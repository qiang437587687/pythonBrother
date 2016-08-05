
# 这个是一个 用户端的 socket

import socket
import time
host = 'localhost'
port = 8083
BUF_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

client.connect((host, port))

while True:
    client.send('hello world\r\n'.encode())
    print('send data')
    time.sleep(1)


# while True:
#     dataR = client.recv(BUF_SIZE)
#     print(dataR.decode())


