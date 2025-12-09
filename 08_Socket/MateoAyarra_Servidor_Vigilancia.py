import socket
import json
import threading as t

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


opc = ''

def updateOpc():
    global opc
    while not opc == '-1':
        opc = input('Introduzca -1 para salir: ')

#TODO: implementar envio con diccionario para poder detectar mas de un coche a la vez
def server():
    global opc
    sock = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
    sock.bind((IP, PUERTO))
    sock.listen(1)
    sock.settimeout(1)

    while not opc == '-1':
        try:
            conn, addr = sock.accept()
            data = conn.recv(1024).decode()
            #Si no esta en data no le importa
            if data in conteo:
                conteo[data] = conteo[data] + 1
                print(f'Se detecto un(a) {data}, en total se detectaron {conteo[data]}')
        #Obligamos a que el accept no bloquee los procesos aunq no haya cliente
        except socket.timeout:
            continue

def main():
    servidor = t.Thread(target=server, args=())
    controlador = t.Thread(target=updateOpc, args=())

    servidor.start()
    controlador.start()

    servidor.join()
    controlador.join()

if __name__ == '__main__':
    main()