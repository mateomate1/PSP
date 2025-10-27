import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8080

conteo = {"persona": 0, "coche": 0, "moto": 0, "bicicleta": 0}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))

print(f"Servidor UDP esperando en {UDP_IP}:{UDP_PORT}...")

while True:
    data, addr = server_socket.recvfrom(1024)  
    objeto = data.decode()

    if objeto in conteo:
        conteo[objeto] += 1
        print(f"Detectado: {objeto} - Total: {conteo[objeto]}")

server_socket.close()
