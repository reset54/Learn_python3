# взято с 
# https://www.youtube.com/watch?v=ZGfv_yRLBiY&ab_channel=%D0%9E%D0%BB%D0%B5%D0%B3%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%BE%D0%B2

# socket - это пара, (домен:порт)
# через порт осуществляется взаимодействие между 2мя субъектами (клиент-сервер)
# AF_INET - IPv4
# SOCK_STREAM - TCP

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen()


while(True):
    print('Before .accept()')
    server_socket.accept()# -> tuple
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    while(True):
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)
