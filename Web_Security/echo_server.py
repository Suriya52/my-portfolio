import socket

# Define server host and port
host = '127.0.0.1'  # Localhost
port = 65432        # Port to bind to

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Enable the server to accept connections (maximum number of queued connections is 1)
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}")
    
    # Accept incoming connections
    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            
            # Continuously receive data from the client and send it back
            while True:
                data = conn.recv(1024)  # Buffer size is 1024 bytes
                if not data:
                    break  # If no data is received, exit the loop
                
                # Send back the received data (echo)
                conn.sendall(data)
                print(f"Echoed back: {data.decode()}")
