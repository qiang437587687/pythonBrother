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







