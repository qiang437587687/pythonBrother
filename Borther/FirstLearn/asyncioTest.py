#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("asyncio Test 上一节的那个例子还是没有看懂怎么实现的协程")

import asyncio

# @asyncio.coroutine   # 这个符号的作用是把一个生成器标记成一个coroutine  (coroutine这个单词的意思是协程)
# def hello():
#     print('hello World')
#     # 一步调用asyncio.sleep
#     r = yield from asyncio.sleep(1)
#     print('当前yield的r', r)
#     print('hello agagin')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())  # 这里面执行耗时的操作的时候不会等待  执行别的函数或者进程线程了
# loop.close()


# 从3.5开始可以用async 来替换 @asyncio.coroutine 用 await 来替换yield from
async def hello():
    print('hello world!')
    r = await asyncio.sleep(1)
    print('hello again! %s ' % r)
    print()

@asyncio.coroutine
def wget(host):
    print("wget %s..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))

    writer.close()

loop1 = asyncio.get_ev_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.163.com', 'www.sohu.com']]
loop1.run_until_complete(asyncio.wait(tasks))
loop1.close()


# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()

# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop1.run_until_complete(asyncio.wait(tasks))
# loop1.close()

