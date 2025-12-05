import socket
import json
import multiprocessing
import random

#Variables
IP = '127.0.0.1'
PUERTO = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.sendto('', (IP, PUERTO))

opc = ''

def updateOpc():
    while not opc == '-1':
        opc = input('Introduzca -1 para salir')

def cliente():
    objetos = ["-", "persona", "coche", "moto", "bicicleta"]
    while not opc == '-1':
        obj = random.randint(-10, 4)
        if obj <= 0:
            obj = 0
        objetoDetectado = objetos[obj]


def main():
    print

if __name__ == '__main__':
    main()