import socket 


s = socket.socket()

port = 12345

s.connect(('127.0.0.1',port))

#recieve data from server
print(s.recv(1024))
s.close()
