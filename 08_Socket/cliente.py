import socket
import random
#Variables
ip = '127.0.0.1'
port = 3000

sock = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
sock.connect((ip, port))

while True:
    objetos = ["-", "persona", "coche", "moto", "bicicleta"]
    obj = random.randint(-10, 4)
    if obj <= 0:
        obj = 0
    objetoDetectado = objetos[obj]
    sock.send(objetoDetectado.encode())