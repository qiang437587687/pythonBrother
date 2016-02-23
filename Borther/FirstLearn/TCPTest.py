[]#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('TCPTest')


import socket
import threading
import time

# 创建一个socket

# 创建Socket时候 AF_INET 制定的是用IPv4协议 AF_INET6 是IPv6
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接.(这里面是一个 tuple 注意了)
s.connect(('www.sina.com.cn', 80))

# 发送数据  # 其中 b 可能是表示这里面的转义都不算  r 是正则
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')




# 接收数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

print(data)

s.close()




#  服务器端练习

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9999))

s.listen(5)
print("Waiting for connection...")

while True:
    # 接受一个新的连接
    sock, addr = s.accept()
    # 创建一个新的线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

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


