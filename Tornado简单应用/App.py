#!/usr/bin/env python3
#-*-coding: utf-8-*-


import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import logging

from tornado.options import define, options


define('port', default=8000, type=int)
logging.basicConfig(level=logging.INFO)


class IndexHander(tornado.web.RequestHandler):
    def get(self):
        arg = self.get_argument('q', 'Hello')
        logging.info('type in ' + arg)
        self.write(arg + ' world!')

settings = {'debug': True}  # 开启debug 的参数
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHander)], **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    logging.info('server started...')














