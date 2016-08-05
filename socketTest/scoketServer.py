
# http://blog.csdn.net/rebelqsp/article/details/22109925 这个里面是
# 介绍了详细的socket 函数还有方法.

# 服务端..

import socket

BUF_SIZE = 1024
host = 'localhost'
port = 8083


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port)) # 尼玛啊 服务端用 bing 用户端用 conne
server.listen(1)

client, address = server.accept() # 这个地方设置成了1 所以没有放到循环中

# server.send("dfghj".encode())

while True:
    data = client.recv(BUF_SIZE)
    print(data.decode())









