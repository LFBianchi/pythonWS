import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
flag = True
while flag:
    clientsocket, address = s.accept()
    print(f'Connection with {address[0]} successfull!')
    clientsocket.send(bytes('Welcome to the server!', 'utf-8'))
    clientsocket.close()