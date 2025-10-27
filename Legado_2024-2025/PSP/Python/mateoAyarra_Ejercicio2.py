import multiprocessing
import queue
import random
import time

objetosDetectados = queue.Queue()
personas = 0
vehiculos = 0

def getObjeto():
    objetos = ['-', 'persona', 'coche', 'moto', 'bicicleta']
    obj = random.randint(-10,4)
    obj = 0 if obj < 0 else obj
    objetoDetectado = objetos[obj]
    return objetoDetectado

def camara(ref, camaraID):
    while True:
        objeto = getObjeto()
        objetosDetectados.put(objeto)
        if (objeto != ref):
            personas



def main():
    procesoPersonas = multiprocessing.Queue()
    procesoVehiculos = multiprocessing.Queue()
    procesoCamara = multiprocessing.Process(target=camara, args=())
    

if __name__ == "__main__":
    main()
