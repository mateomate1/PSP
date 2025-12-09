import socket
import time

#127.0.0.1 = localhost
HOST = "127.0.0.1"
PORT = 5000

#Diccionario de conteo de vehiculos
conteo = {
    "persona": 0,
    "coche": 0,
    "moto": 0,
    "bicicleta": 0
}

#Hacer exactamente como en el pdf
sock = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024).decode()
    if not data:
        print('No se recibio nada')
        break
    if data in conteo:
        conteo[data] = conteo[data] + 1
        print("Detectado: " + data + " | Total: " + str(conteo[data]))