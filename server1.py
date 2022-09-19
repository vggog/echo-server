"""
A simple echo-server.
Blocking sockets.
"""

import socket
from config import Config

server_config = Config()


def server():
    server_socket = socket.socket()
    server_socket.bind(
        (server_config.HOST, server_config.PORT)
    )
    server_socket.listen()

    while True:
        conn, add = server_socket.accept()
        data = conn.recv(1024).decode()
        conn.send(data.encode())
        print('Data from client:', data)

        conn.close()


if __name__ == '__main__':
    print('server started')

    try:
        server()
    except KeyboardInterrupt:
        print('\nserver stopped')
