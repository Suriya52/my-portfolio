import socket

# Define server address and port
host = '127.0.0.1'  # Localhost
port = 65432        # Same port as the server

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((host, port))
    print("Connected to server!")

    # Start a loop to continuously send messages
    while True:
        # Take input from the user
        message = input("Enter a message to send (type 'exit' to quit): ")
        
        # If the user types 'exit', break the loop and close the connection
        if message.lower() == 'exit':
            print("Closing connection.")
            break
        
        # Send the message to the server
        client_socket.sendall(message.encode())

        # Receive the echoed message from the server
        data = client_socket.recv(1024)
        print(f"Echoed from server: {data.decode()}")
