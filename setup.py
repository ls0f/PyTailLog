from setuptools import setup


PACKAGE = "pytaillog"
NAME = "pytaillog"
DESCRIPTION = "dispaly log in a browser"
AUTHOR = "lovedboy"
AUTHOR_EMAIL = "lovedboy.tk@qq.com"
URL = "https://github.com/lovedboy/PyTailLog"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    install_requires=[
        "tornado",
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)
