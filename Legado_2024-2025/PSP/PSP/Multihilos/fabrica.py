import random
import threading
from queue import Queue
import time

coches = [
    {'modelo': 'Golf', 'precio': 22000},
    {'modelo': 'Passat', 'precio': 25000},
    {'modelo': 'Polo', 'precio': 19000},
    {'modelo': 'Tiguan', 'precio': 27000}
]

cola = Queue()

def lineaProduccion(idLinea):
    for _ in range(50):
        coche = random.choice(coches)
        cola.put(coche)
        time.sleep(random.uniform(0.1, 0.5))

def concesionario(idConcesionario):
    while True:
        if not cola.empty():
            coche = cola.get()
            print(f"Concesionario {idConcesionario} ha conseguido el coche: {coche['modelo']} por {coche['precio']}€")
        else:
            time.sleep(1)

def main():
    numLineas = int(input("Cuantas lineas de produccion deseas arrancar? "))
    numConcesionarios = int(input("Cuantos concesionarios deseas arrancar? "))

    hilosProduccion = []
    for i in range(numLineas):
        hilo = threading.Thread(target=lineaProduccion, args=(i+1,))
        hilosProduccion.append(hilo)
        hilo.start()

    hilosConcesionarios = []
    for i in range(numConcesionarios):
        hilo = threading.Thread(target=concesionario, args=(i+1,))
        hilosConcesionarios.append(hilo)
        hilo.start()

    for hilo in hilosProduccion:
        hilo.join()

    for hilo in hilosConcesionarios:
        hilo.join()

if __name__ == "__main__":
    main()
