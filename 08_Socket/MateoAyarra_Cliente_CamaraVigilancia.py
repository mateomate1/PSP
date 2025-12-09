import socket

HOST = "0.0.0.0"
PORT = 5000

conteo = {
    "persona": 0,
    "coche": 0,
    "moto": 0,
    "bicicleta": 0
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    mensaje = data.decode()
    if mensaje in conteo:
        conteo[mensaje] = conteo[mensaje] + 1
        print("Detectado: " + mensaje + " | Total: " + str(conteo[mensaje]))
