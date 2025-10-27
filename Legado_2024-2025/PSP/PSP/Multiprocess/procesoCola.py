from multiprocessing import Queue, Process

def escritor(cola, texto):
    cola.put(texto)

def lector(cola):
    texto = cola.get()
    print(f"Contenido de la cola:\t{texto}")

def main():
    cola = Queue(maxsize=1000)
    texto = input("Escriba aqui su texto (-1 para terminar): ")
    
    while texto != '-1':
        procesoEscritor = Process(target=escritor, args=(cola, texto))
        procesoEscritor.start()
        procesoEscritor.join()

        procesoLector = Process(target=lector, args=(cola,))
        procesoLector.start()
        procesoLector.join()

        texto = input("Escriba aqui su texto (-1 para terminar): ")

    print("Programa terminado.")

if __name__ == "__main__":
    main()
