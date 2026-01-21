import socket
import threading

def receive_messages(client):
    while True:
        msg = client.recv(1024).decode()
        if not msg:
            break
        print("Server:", msg)

def send_messages(client):
    while True:
        msg = input("")
        client.send(msg.encode())

client = socket.socket()
client.connect(('192.168.56.1', 5000))

recv_thread = threading.Thread(target=receive_messages, args=(client,))
send_thread = threading.Thread(target=send_messages, args=(client,))

recv_thread.start()
send_thread.start()




"""import socket
import threading

def receive_messages(client):
    while True:
        msg = client.recv(1024).decode()
        if not msg:
            break
        print("Server:", msg)

def send_messages(client):
    while True:
        msg = input("")
        client.send(msg.encode())

client = socket.socket()
client.connect(("152.57.203.76", 5000))  # ← Change this

# Start threads
threading.Thread(target=receive_messages, args=(client,)).start()
threading.Thread(target=send_messages, args=(client,)).start()"""
