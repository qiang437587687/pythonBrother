#!/usr/bin/env python3
#-*-coding: utf-8-*-

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import logging

from tornado.options import define, options

define('port', default=8001, help='run on the given port', type=int)
logging.basicConfig(level=logging.INFO)


class IndexHander(tornado.web.RequestHandler):
    def get(self):
        self.render('index1.html')


class ContentHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        n1 = self.get_argument('n1')
        n2 = self.get_argument('n2')
        n3 = self.get_argument('n3')
        n4 = self.get_argument('n4')
        self.render('content1.html', n1=n1, n2=n2, n3=n3, n4=n4)


settings = {'debug': True}  # 开启debug 的参数
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHander), (r'/content', ContentHandler)],
                                  template_path=os.path.join(os.path.dirname(__file__), 'Temporary'),
                                  static_path=os.path.join(os.path.dirname(__file__), "static"),
                                  **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    logging.info('server started...')


























