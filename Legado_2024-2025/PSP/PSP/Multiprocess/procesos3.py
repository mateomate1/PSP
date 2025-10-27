import multiprocessing as mp

def escritor(nomFich, texto):
    with open(nomFich, "a") as fichero:
        fichero.write(texto + "\n")

def lector(nomFich):
    with open(nomFich, "r") as fichero:
        contenido = fichero.read()
    print(f"Contenido del fichero:\t{contenido}")

def main():
    nomFich = "fichero.txt"
    texto = input("Escriba aqui su texto (-1 para terminar): ")
    
    while texto != '-1':
        procesoEscritor = mp.Process(target=escritor, args=(nomFich, texto))
        procesoEscritor.start()
        procesoEscritor.join()

        procesoLector = mp.Process(target=lector, args=(nomFich,))
        procesoLector.start()
        procesoLector.join()

        texto = input("Escriba aqui su texto (-1 para terminar): ")

    print("Programa terminado.")

if __name__ == "__main__":
    main()
