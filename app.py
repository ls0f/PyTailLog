#!/usr/bin/python


import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import sys
import select
import os

PORT = int(sys.argv[1])
LISTENERS = []


def check_file():

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
        print "WebSocket open"
        LISTENERS.append(self)
 
    def on_message(self, message):
        pass
 
    def on_close(self):
        print "WebSocket close"
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
    "debug":True,
    }

application = tornado.web.Application([
    (r'/tail/', TailHandler),
    (r'/', IndexHandler),
], **settings)
 
if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT)
 
    tailed_callback = tornado.ioloop.PeriodicCallback(check_file, 500)
    tailed_callback.start()
 
    io_loop = tornado.ioloop.IOLoop.instance()
    try:
        io_loop.start()
    except SystemExit, KeyboardInterrupt:
        io_loop.stop()
