import socket

HOST = "localhost"
PORT = 8023

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
conn, address = s.accept()

while True:
    data = conn.recv(1024)

    print(data.decode())

    if len(repr(data)) == 0:
        conn.sendall("done".encode())
    else:
        conn.sendall("no done".encode())

# while True:
#     conn, addr = s.accept()
#     print("connected" + addr)
#
#     while True:
#         data = conn.recv(1024)
#
#         print(data)
#         # if len(repr(data)) == 0:
#         #     conn.sendall("done")
#         # else:
#         #     conn.sendall("no done")

conn.close()


