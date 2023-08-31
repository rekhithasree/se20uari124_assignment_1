import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6666))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from{address}has been established")
    clientsocket.send(bytes("a message from server","utf-8"))