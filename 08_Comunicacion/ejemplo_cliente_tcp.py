'''
Tenemos una cámara de vigilancia que detecta diversos tipos de objetos: persona, coche, moto y bicicletas.

En otra máquina (puede ser la misma para desarrollo), tenemos un programa que recibe el resultado de la detección de la cámara y contabiliza los objetos. 

Se pide:

Programa Python que levanta un socket y contabiliza en la información que recibe cuántos objetos se han detectado. Imprime un mensaje en pantalla cada vez que detecta un objeto.
Otro programa simula la cámara mediante un mecanismo aleatorio y envía por el socket anterior lo que detecta la cámara simulada. Puede usarse - si se quiere, no es obligatorio - el siguiente código que hace que el número de detecciones no sea homogéneo.
 objetos = ['-', 'persona', 'coche', 'moto', 'bicicleta']
 obj = random.randint(-10,4)
 if obj <= 0:
    obj = 0
 objetoDetectado = objetos[obj]


Ambos programas pueden tener un bucle infinito o limitado a un número máximo de n iteraciones.
'''

import socket
import time
import random

HOST = "127.0.0.1"
PORT = 5000

objetos = ["-", "persona", "coche", "moto", "bicicleta"]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

opc = '0'
while not '-1':
    obj = random.randint(-10, 4)
    if obj <= 0:
        obj = 0
    objetoDetectado = objetos[obj]

    if objetoDetectado != "-":
        sock.sendall(objetoDetectado.encode())

    time.sleep(0.5)

sock.shutdown(socket.SHUT_RDWR)
sock.close()