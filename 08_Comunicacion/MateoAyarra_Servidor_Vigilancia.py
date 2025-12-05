import socket
import json
import multiprocessing as mp

#Variables
IP = '127.0.0.1'
PUERTO = 3000
#Al hacer un mapa podemos definir lo que detecta
conteo = {
    'persona': 0,
    'coche': 0,
    'moto' : 0,
    'bicicleta' : 0
}

sock = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
sock.bind(IP, PUERTO)
sock.listen()
conn, addr = sock.accept()

opc = ''

def updateOpc():
    while not opc == '-1':
        opc = input('Introduzca -1 para salir')

#TODO: implementar envio con diccionario para poder detectar mas de un coche a la vez
def server():
    while not opc == '-1':
        data = conn.recv(1024)
        #Si no esta en data no le importa
        if data in conteo:
            conteo[data] = conteo[data] + 1
            print(f'Se detecto un(a) {data}, en total se detectaron {conteo[data]}')

def main():
    servidor = mp.Process(target=server)
    controlador = mp.Process(target=updateOpc)

    servidor.start()
    controlador.start()

if __name__ == '__main__':
    main()