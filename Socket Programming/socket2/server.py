import socket


#creating socket object
s = socket.socket()
print ("Socket created successfully")

port = 12345


s.bind(('',port))     #empty string - listen to reqs coming from other computers
print ("socket binded to %s" %(port))



#put socket into listening mode 
s.listen(5)
print ("socket is listening")


while True :

    #establish connection wirh client
    c,addr = s.accept()
    print ('Got connection from',addr) 

    c.send(b"Thanks for connecting")
    c.close()
