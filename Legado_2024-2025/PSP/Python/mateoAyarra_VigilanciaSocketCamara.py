import socket
import random
import time

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 9999))

objetos = ["-", "persona", "coche", "moto", "bicicleta"]

try:
    for _ in range(20):
        obj = random.randint(-10, 4)
        if obj <= 0:
            obj = 0
        time.sleep(1)
except:
    cliente.close()
