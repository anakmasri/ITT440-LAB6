import socket

ClientSocket = socket.socket()
host = '192.168.1.104'
port = 8888

print('\nWiting for connection....')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))


Response = ClientSocket.recv(1024)
print(Response)
while True:
        Input = input('')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))

ClientSocket.close()
