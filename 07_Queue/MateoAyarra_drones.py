'''
Vamos a implementar un centro de control de drones de vigilancia que realizará las siguientes operaciones:

Despegará drones.
Activará el centro de control.
Pedirá al usuario órdenes para coordinar las operaciones.
Presentará en pantalla las alarmas.
Consta de un hilo principal, un hilo de centro de control y un hilo por cada dron.

El hilo principal se encarga de :

Crear las estructuras de datos necesarias para comunicación y pasárselas a los procesos:
Lista de Alarmas, donde los drones añaden las alarmas (append) y el centro de control las extrae (pop)
Lista de Control, donde el centro de control añade las órdenes y los drones las reciben.
Cada lista estará protegida por un lock específico.
Arrancar el hilo que lleva a cabo el centro de control
Pedirle al usuario órdenes y llevarlas a cabo: 2 órdenes
Despegar: Activará un nuevo dron (Crear el hilo)
Aterrizar: Aterrizará un dron (uno cualquiera). Para aterrizar el dron le mandará un mensaje por la lista de control
El centro de control recibirá las alertas de los drones por la lista de alarmas y sacará un mensaje en pantalla con la alerta

Cada dron:

Está identificado por un número entero (por ejemplo de 1 a 4).
Se implementa con un hilo independiente
Llama a la función vigilancia y recibe una alarma (Ver función abajo).
Si la alarma no es "Calma" creará una estructura dict con su ID y la alarma y la pondrá en la lista de alarmas
De vez en cuando consultará la lista de control y si hay una orden de "Aterrizar" terminará el proceso
Código de ayuda: Vigilancia:

def vigilaHorizonte():
    situacion = ['Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Alarma leve', 'Alarma Media', 'Alarma Grave']
    i = random.randint(0, 9)
    return(situacion[i])
'''
import time
import queue
import random
import threading

listaDrones = {}
listaAlarmas = queue.Queue()
listaControl = queue.Queue()
lock = threading.Lock()
encendido = True

def despegar():
    print('Despegar')

def vigilaHorizonte():
    situacion = ['Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Alarma leve', 'Alarma Media', 'Alarma Grave']
    i = random.randint(0, 9)
    return(situacion[i])

def dron(id):
    continuar = True
    while(continuar and encendido):
        time.sleep(0.5)
        lock.acquire()
        orden = ''
        if(not listaControl.empty()):
            orden = listaControl.get()
        if(orden == id):
            continuar = False
            lock.release()
        else:
            if(orden != ''):
                listaControl.put(orden)
            lock.release()
            situacion = vigilaHorizonte()
            #creará una estructura dict con su ID y la alarma y la pondrá en la lista de alarmas
            if(situacion != 'Calma'):
                mapa = {id, situacion}
                listaAlarmas.put(mapa)
                print(mapa)


def apagarDron():
    claves = listaDrones.keys()
    print(f'Se procede a listar los drones:')
    for clave in claves:
        print(f'Identificador: {clave}')
    id = int(input('Inserte el identificador del dron a apagar:'))
    if(id in listaDrones.keys()):
        listaDrones.pop(id)
        listaControl.put(id)
    else:
        print('Identificador invalido')

def despegarDron():
    id = random.randint(0, len(listaDrones))
    while id in listaDrones.keys():
        id = random.randint(0, len(listaDrones))
    t = threading.Thread(target=dron, args=(id,))
    t.start()
    listaDrones[id] = t


def main():
    global encendido
    opc = 0
    while (opc != '3'):
        opc = input('Inserte una instruccion(1: Despegar nuevo dron, 2: Apagar dron 3: Salir):')
        if(opc == '1'):
            despegarDron()
        elif(opc == '2'):
            apagarDron()
        elif(opc == '3'):
            encendido = False
            print('Se procede a imprimir todas las alarmas de la cola:')
            while not listaAlarmas.empty():
                alarma = listaAlarmas.get()
                print(alarma)
        else:
            print('Orden no reconocida')

if(__name__ == "__main__"):
    main()