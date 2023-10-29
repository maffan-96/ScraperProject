import socket
from .fast_html import create_html

def port_run(apartments):
    # Define socket host and port
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 8085

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set socket options for reusing the address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the host and port
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    
    # Listen for incoming connections
    server_socket.listen(1)

    # Convert image URLs to HTML img tags
    for row in apartments:
        row["img_url"] = f'<img src="{row["img_url"]}" width="320" height="240">'

    while True:
        print('**************************************')
        
        # Accept incoming client connections
        client_connection, client_address = server_socket.accept()
        
        # Receive the client's request
        request = client_connection.recv(1024).decode()
        
        # Generate an HTML response using create_html and send it back to the client
        response = f'HTTP/1.0 200 OK\n\n{create_html(apartments)}'
        client_connection.sendall(response.encode("windows-1250"))
        
        # Close the client connection
        client_connection.close()
