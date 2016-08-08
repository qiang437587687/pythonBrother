
# http://blog.csdn.net/rebelqsp/article/details/22109925
# 这个连接里面很详细的介绍了相关的python socket函数等.

import socket
import time
HOST = "localhost"
PORT = 8023

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

d = 1

while True:

    strrrr = "nimei"
    s.sendall(strrrr.encode())

    data = s.recv(1024)
    print(data.decode())
    time.sleep(1)

s.close()







