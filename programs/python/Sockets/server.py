import socket
import threading

def receive_messages(conn):
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print("Client:", msg)

def send_messages(conn):
    while True:
        msg = input("")
        conn.send(msg.encode())

server = socket.socket()
server.bind(('0.0.0.0', 5000))
server.listen()

print("Server waiting for connection...")
conn, addr = server.accept()
print("Connected with:", addr)

recv_thread = threading.Thread(target=receive_messages, args=(conn,))
send_thread = threading.Thread(target=send_messages, args=(conn,))

recv_thread.start()
send_thread.start()
