import random
import threading
from queue import Queue

colaPar = Queue()
colaImpar = Queue()

def pares():
    pares = colaPar.get()
    with open("pares.dat", "a") as fichero:
        fichero.write(f'{pares} ')

def impares():
    impares = colaImpar.get()
    with open("impares.dat", "a") as fichero:
        fichero.write(f'{impares} ')

def main():
    n = 0
    for i in range(30):
        n = random.randint(0,20)
        if(n%2 == 0):
            colaPar.put(n)
        else:
            colaImpar.put(n)

    hilos = []
    hilo = threading.Thread(target=pares, args=())
    hilos.append(hilo)
    hilo.start()

    hilos = []
    hilo = threading.Thread(target=impares, args=())
    hilos.append(hilo)
    hilo.start()

    for hilo in hilos:
        hilo.join()

if __name__ == "__main__":
    main()