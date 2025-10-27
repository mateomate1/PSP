import threading

texto = ""

def escritor1(mitad1):
    global texto
    texto += mitad1

def escritor2(mitad2):
    global texto
    texto += mitad2 + " "

def lector():
    print(texto)

def main():

    cad = input('Introduce texto (-1 para terminar) ->')

    while cad != '-1':
        mitad1 = cad[:len(cad)//2]
        mitad2 = cad[len(cad)//2:]

        hiloEscritor1 = threading.Thread(target=escritor1, args=(mitad1,))
        hiloEscritor2 = threading.Thread(target=escritor2, args=(mitad2,))
        hiloLector = threading.Thread(target=lector)

        hiloEscritor1.start()
        hiloEscritor2.start()
        hiloLector.start()

        hiloEscritor1.join()
        hiloEscritor2.join()
        hiloLector.join()

        cad = input('Introduce texto (-1 para terminar) ->')

if __name__ == "__main__":
    main()
