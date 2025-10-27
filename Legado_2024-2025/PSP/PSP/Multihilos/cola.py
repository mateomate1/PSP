import threading
from multiprocessing import Queue

cola = Queue()

def escritor(idHilo):
    while True:
        texto = input(f'Hilo {idHilo}, introduce un texto (-1 para terminar): ')
        if texto == '-1':
            cola.put('0x01')
            return
        else:
            cola.put(texto)

def lector():
    while True:
        texto = cola.get()
        if texto == '0x01':
            print('Fin del programa')
            return
        else:
            print(f'Texto recibido: {texto}')

def main():
    hiloEscritor1 = threading.Thread(target=escritor, args=(1,))
    hiloEscritor2 = threading.Thread(target=escritor, args=(2,))
    hiloLector = threading.Thread(target=lector)

    hiloEscritor1.start()
    hiloEscritor2.start()
    hiloLector.start()

    hiloEscritor1.join()
    hiloEscritor2.join()
    hiloLector.join()

if __name__ == "__main__":
    main()
