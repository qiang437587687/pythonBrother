#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print('WSGI test this is a server')

from wsgiref.simple_server import make_server

from HelloTEST import application

httpd = make_server('', 8000, application)
print('Serving Http on port 8000....')
httpd.serve_forever()

















