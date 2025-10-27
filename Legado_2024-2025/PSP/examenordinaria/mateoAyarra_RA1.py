import random
from multiprocessing import Process

def pares(n):
    with open("pares.dat", "a") as fichero:
        fichero.write(f'{n} ')

def impares(n):
    with open("impares.dat", "a") as fichero:
        fichero.write(f'{n} ')

def main():
    for i in range(30):
        n = random.randint(0,20)

        if n % 2 == 0:
            procesoPares = Process(target=pares, args=(n,))
            procesoPares.start()
            procesoPares.join()

        else:
            procesoImpares = Process(target=impares, args=(n,))
            procesoImpares.start()
            procesoImpares.join()

if __name__ == "__main__":
    main()