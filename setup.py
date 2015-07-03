from setuptools import setup,find_packages


PACKAGE = "pytaillog"
NAME = "pytaillog"
DESCRIPTION = "dispaly log in a browser"
AUTHOR = "lovedboy"
AUTHOR_EMAIL = "lovedboy.tk@qq.com"
URL = "https://github.com/lovedboy/PyTailLog"
VERSION = '0.1'

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
    scripts=['bin/pytaillog'],
    include_package_data = True,
    packages = find_packages(),
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    zip_safe=False,
)
