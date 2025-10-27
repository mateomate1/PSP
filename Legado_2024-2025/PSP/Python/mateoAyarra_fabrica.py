'''
Trabajamos el problema productor - consumidor.

Tenemos una fábrica de modelos de coches que los fabrica y pone a disposición de los concesionarios. 

Por otro lado los concesionarios van tomando los coches en el orden que viene de la fábrica para venderlos

Realizar un programa que modele la situación teniendo en cuenta que:
- La fábrica puede tener una o varias líneas de producción. Cada línea de producción es un hilo que fabrica coches aleatoriamente.
- Los coches que fabrica son cuatro modelos: ['Golf', 'Passat', 'Polo', 'Tiguan']. Cada modelo lleva asociado su precio.
- Cada línea de producción coloca en la cola el modelo y precio. Por ejemplo: {'modelo':'Polo', 'precio':19000}
- Cada concesionario es un hilo que lee de la cola e imprime en pantalla qué modelo ha conseguido y a qué precio. Si no hay coches pone en pantalla que no encuentra coches.
- El hilo principal pedirá al usuario cuántas líneas de producción quiere arrancar y cuántos concesionarios. Cada línea de producción fabricará 50 coches y morirá.
'''

import threading
import random
import queue
import time

cola = queue.Queue()

MODELOS = [
    {"modelo": "Golf", "precio": 23000},
    {"modelo": "Passat", "precio": 27000},
    {"modelo": "Polo", "precio": 19000},
    {"modelo": "Tiguan", "precio": 32000}
]

def linea_produccion(id_linea):
    while (True):
        coche = random.choice(MODELOS)
        print(f"Línea {id_linea} ha fabricado: {coche['modelo']} por {coche['precio']}€, hau un total de {cola.qsize()} coches disponibles.")
        cola.put(coche)
        time.sleep(5)

def concesionario(id_concesionario):
    while(True):
        if not cola.empty():
            coche = cola.get()
            print(f"Concesionario {id_concesionario} ha vendido: {coche['modelo']} por {coche['precio']}€")
        else:
            print(f"Concesionario {id_concesionario}: No hay coches disponibles.")
        time.sleep(3)


def main():
    n_lineas = int(input("Numero de lineas de produccion a arrancar: "))
    n_concesionarios = int(input("Numero de concesionarios a abrir: "))
    
    lineas = []
    concesionarios = []
    
    for i in range(n_lineas):
        lineas.append(threading.Thread(target=linea_produccion, args=(i+1,)))
    
    for i in range(n_concesionarios):
        concesionarios.append(threading.Thread(target=concesionario, args=(i+1,)))

    for linea in lineas:
        linea.start()
    
    for con in concesionarios:
        con.start()

    for linea in lineas:
        linea.join()
    
    for con in concesionarios:
        con.join()


if __name__ == "__main__":
    main()
