import os
import re

from setuptools import setup, find_packages


def read(filename):
    return open(filename).read()

BASE_PATH = os.path.join(os.path.dirname(__file__), "flask_admin_utils")
INIT_PATH = os.path.join(BASE_PATH, "__init__.py")
INIT_TEXT = read(INIT_PATH)


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, INIT_TEXT)
    return strval

setup(
    name="Flask-Admin-Utils",
    version=grep('__version__'),
    description="Utils for Flask-Admin",
    long_description=read("README.md"),
    author=grep('__author__'),
    author_email=grep('__author__'),
    license="BSD",
    url="https://github.com/andrix/flask-admin-utils",
    packages=find_packages(),
    platforms='any',
    install_requires=[
        "flask-admin",
        "sqlalchemy-utils",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
