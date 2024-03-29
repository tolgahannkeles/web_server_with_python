from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assigning a server socket
serverPort = 6789
serverSocket.bind(('192.168.1.105', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        with open(filename[1:], 'r') as f:
            outputdata = f.read()

        # Send HTTP header line into the socket
        connectionSocket.sendall("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the client
        connectionSocket.sendall(outputdata.encode())
    except FileNotFoundError:
        # Send response message for file not found
        connectionSocket.sendall("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.sendall("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
    except Exception as e:
        print("Error:", e)
    finally:
        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
