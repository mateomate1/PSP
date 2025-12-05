import socket
import time
import random

HOST = "127.0.0.1"
PORT = 5000

objetos = ["-", "persona", "coche", "moto", "bicicleta"]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    obj = random.randint(-10, 4)
    if obj <= 0:
        obj = 0
    objetoDetectado = objetos[obj]

    if objetoDetectado != "-":
        sock.sendto(objetoDetectado.encode(), (HOST, PORT))

    time.sleep(0.5)
