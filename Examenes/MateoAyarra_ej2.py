import threading
import random
import queue
import time

alarmas = queue.Queue()
listaControl = queue.Queue()
lock = threading.Lock()
hilos = []

def vigilaHorizonte():
    objetos = ['nada', 'persona', 'coche', 'moto', 'bicicleta']
    obj = random.randint(-10, 4)
    obj = 0 if obj < 0 else obj
    return(objetos[obj])

def camaraPersona(id):
    iteracion = 0
    objetosDetectados = 0
    encendido = True
    while encendido:
        situacion = vigilaHorizonte()
        print(f'Se ha detectado {situacion}')
        if iteracion > 200:
            listaControl.put({id, -1})
        if (not listaControl.empty()):
            control = listaControl.get()
            if (control == {id, -1}):
                encendido = False
                print(f'Soy el hilo {id} y llevo {objetosDetectados} persona(s)')
            else:
                listaControl.append(control)
        if(encendido):
            if(situacion == 'persona'):
                objetosDetectados += 1
            iteracion += 1

def camaraVehiculo(id):
    iteracion = 0
    objetosDetectados = 0
    encendido = True
    while encendido:
        situacion = vigilaHorizonte()
        print(f'Se ha detectado {situacion}')
        if iteracion > 200:
            listaControl.put({id, -1})
        if (not listaControl.empty()):
            control = listaControl.get()
            if (control == {id, -1}):
                encendido = False
                print(f'Soy el hilo {id} y llevo {objetosDetectados} persona(s)')
            else:
                listaControl.append(control)
        if(encendido):
            if(situacion == 'coche' or situacion == 'moto' or situacion == 'bicicleta'):
                objetosDetectados += 1
            iteracion += 1

def main():
    t1 = threading.Thread(target=camaraPersona, args=(1,))
    hilos.append(t1)
    t1.start()

    t2 = threading.Thread(target=camaraVehiculo, args=(1,))
    hilos.append(t2)
    t2.start()


if __name__ == '__main__':
    main()