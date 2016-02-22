#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)
#
import asyncio, os, json, time
#
from datetime  import datetime

from aiohttp import web
#
def index(request):
    return web.Response(body=b'<h1>Welcome Awesome</h1>')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)  # 这个地方的是router.add_route 不是 add_router 这个要看好了要不然会出错的.
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', '9000')
    logging.info('startd at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()






