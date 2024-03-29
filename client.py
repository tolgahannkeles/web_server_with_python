import sys
import socket

def http_client(server_host, server_port, filename):
    # Create a TCP socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        clientSocket.connect((server_host, server_port))
        
        # Send HTTP GET request
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
        clientSocket.sendall(request.encode())
        
        # Receive and print the response
        response = b""
        while True:
            data = clientSocket.recv(4096)
            if not data:
                break
            response += data

        print("Server Response:")
        print(response.decode())
    
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the socket
        clientSocket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py server_host server_port filename")
        sys.exit(1)

    server_host = sys.argv[1] #first arg
    server_port = int(sys.argv[2]) #second arg
    filename = sys.argv[3] # third arg
    
    http_client(server_host, server_port, filename)
