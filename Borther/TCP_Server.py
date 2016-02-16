#!/usr/bin/env python3
# -*- coding: utf-8 -*-



#  服务器端练习

import socket
import threading
import time

#  服务器端练习

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 9999))
ss.listen(5)
print("Waiting for connection...")



def tcplink(sock, addr):
    print('Appect new connection from %s:%s...' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connect from %s:%s closed.' % addr)


while True:
    # 接受一个新的连接
    sock, addr = ss.accept()
    # 创建一个新的线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()



