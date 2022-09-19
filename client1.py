"""
Client for echo-server with blocking sockets.
"""

import socket
from config import Config

client_config = Config


def client_program():
    client_socket = socket.socket()
    client_socket.connect(
        (client_config.HOST, client_config.PORT)
    )
    client_socket.send('Hello, world!!!'.encode())
    data = client_socket.recv(1024).decode()

    print('Data from server:', data)

    client_socket.close()


if __name__ == '__main__':
    client_program()
