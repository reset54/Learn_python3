import socket


IP = "127.0.0.1"
PORT = 8001

server = socket.create_server((IP, PORT))

server.setsockopt(
    socket.SOL_SOCKET, 
    socket.SO_REUSEADDR, 
    1
)

server.listen(10)
client_socket, address = server.accept()
received_data = client_socket.recv(1024).decode("utf-8")

print("Получили данные по соккету", received_data)