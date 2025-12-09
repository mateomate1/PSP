import socket
import json
import threading as t
import random

#Variables
IP = '127.0.0.1'
PUERTO = 3000


opc = ''

def updateOpc():
    global opc
    while not opc == '-1':
        opc = input('Introduzca -1 para salir')

def cliente():
    global opc
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PUERTO))
    objetos = ["-", "persona", "coche", "moto", "bicicleta"]
    while not opc == '-1':
        obj = random.randint(-10, 4)
        if obj <= 0:
            obj = 0
        objetoDetectado = objetos[obj]
        sock.send(objetoDetectado.encode())


def main():
    client = t.Thread(target=cliente, args=())
    controlador = t.Thread(target=updateOpc, args=())

    client.start()
    controlador.start()

if __name__ == '__main__':
    main()