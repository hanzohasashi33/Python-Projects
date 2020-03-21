import socket

HOST = '127.0.0.1'     #standard interface address
PORT = 65432           #port to listen on (>1023)


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :     #socket.socket creates a socket opject
    #parameters specify address family and socket type
    #AF_INET internet address family for IPv4 
    #SOCK_STREAM socket type for TCP
    s.bind((HOST,PORT))    #bind() is used to associate socket with address and port no
    #AF_INET requires a 2tuple (host,port)
    s.listen()              #makes it a listening socket
    conn,addr = s.accept()  #gives host and port of connecting entity
    with conn :             #with is used to automatically close the socket at the end
        print('connected by',addr)
        while True :
            data = conn.recv(1024)
            if not data : 
                break
            conn.sendall(data)
