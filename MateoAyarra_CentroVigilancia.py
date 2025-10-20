'''
Vamos a implementar un centro de vigilancia con cámaras que consta de un proceso principal  y un proceso por cada cámara.

El proceso principal se encarga de :

Crear las colas necesarias para comunicación: cola de alarmas y cola de control.
Crear 5 cámaras de vigilancia (1 proceso por cada cámara). En la creación le pasará su ID y las colas de comunicación
Recibir las alertas de cada cámara por la cola de alarmas y ponerlas en pantalla: Ejemplo: Cámara 3 alerta leve.
Contar las alertas de cada cámara y cuando tenga 4 apagar la cámara enviando una orden de "Apágate" por la cola de control
Cada cámara:

Está identificado por un número entero (por ejemplo de 1 a 5).
Se implementa con un proceso independiente del SO
Llama a la función vigilaHorizonte y recibe una alarma (Ver función abajo).
Si la alarma no es "Calma" creará una estructura dict con su ID y la alarma y la pondrá en la cola de alarmas
De vez en cuando consultará la cola de control y si hay una orden de "Apágate" terminará el proceso
Código de ayuda: Vigilancia:

def vigilaHorizonte():
    situacion = ['Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Alarma leve', 'Alarma Media', 'Alarma Grave']
    i = random.randint(0, 9)
    return(situacion[i])
'''
import threading
import random
import time

alarmas = []
lista_control = [] #Aqui se insertan las ordenes de apagado
hilos = []

def vigilaHorizonte():
    situacion = ['Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Alarma leve', 'Alarma Media', 'Alarma Grave']
    i = random.randint(0, 9)
    return(situacion[i])

def camara(camId):
    encendido = True
    while encendido:
        time.sleep(2)
        situacion = vigilaHorizonte()
        if (situacion != 'Calma'):
            alarma = {camId: situacion}
            alarmas.append(alarma)
            print(alarma)
        if lista_control:
            control = lista_control.pop()
            if (control == 'Apagate'):
                encendido = False
                print('Se ha apagado la alarma {camId}')


def main():
    for i in range(5):
        t = threading.Thread(target=camara, args=(i,))
        hilos.append(t)
        t.start()
    opc = '0'
    while opc != 'exit':
        opc = input('Indique lo que quiere hacer(apaga para apagar una camara y exit para salir): ')
        if (opc != 'exit'):
            lista_control.append(opc)

if __name__ == '__main__':
    main()
