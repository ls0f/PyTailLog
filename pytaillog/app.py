#!/usr/bin/python


import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import sys
import select
import os
from optparse import OptionParser

LISTENERS = []

def read_file():

    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline()
        if line:
            print line,
            for element in LISTENERS:
                element.write_message(line.rstrip())
        else: # an empty line means stdin has been closed
            return


class TailHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket open")
        LISTENERS.append(self)
 
    def on_message(self, message):
        pass
 
    def on_close(self):
        print("WebSocket close")
        try:
            LISTENERS.remove(self)
        except:
            pass

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html', host=self.request.host)
 
site_root = os.path.dirname(__file__)
settings = {
    "static_path":os.path.join(site_root,'static'),
    "template_path":os.path.join(site_root,'templates'),
    "debug":False,
    }

application = tornado.web.Application([
    (r'/tail/', TailHandler),
    (r'/', IndexHandler),
], **settings)

def server(host, port):
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port=port, address=host)

    tailed_callback = tornado.ioloop.PeriodicCallback(read_file, 500)
    tailed_callback.start()

    io_loop = tornado.ioloop.IOLoop.instance()
    try:
        io_loop.start()
    except SystemExit, KeyboardInterrupt:
        io_loop.stop()

def main():
    parse = OptionParser(version='pytaillog 0.1')
    parse.add_option('-H','--host', help="listen host, default 0.0.0.0",default='0.0.0.0')
    parse.add_option('-P','--port', help="listen port, default 8080",default=8080, type="int")
    (options,args) = parse.parse_args()

    host = options.host
    port = options.port
    server(host, port)

if __name__ == '__main__':

    main()

