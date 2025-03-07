import socket

s = socket.socket()
print("Socket Created")

s.bind(('localhost',8888))  # s - server   Bind to localhost on port 9999

s.listen(3)
print("Wating for Connection")

while True:
    c, addr = s.accept()                 # c - client     Accept a connection
    
    name = c.recv(1024).decode()
    
    print("Connected with", addr,name)

    c.send(bytes('Welcome to ......','utf-8'))

    c.close()