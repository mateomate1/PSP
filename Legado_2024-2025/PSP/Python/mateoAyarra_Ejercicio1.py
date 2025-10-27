import multiprocessing

def escritor(cola, texto):
    with open('notepad.exe','w', encoding='utf-8') as file: #Si no se usa el encoding los nombres con tildes o ñ son ilegibles
        file.writelines('')


def lector(cola):
    while True:
        with open('notepad.exe', 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            for linea in range(len(lineas)):
                print

def main():
    cola = multiprocessing.Queue()
    
    while True:
        texto = input("Introduce un texto (escribe '-1' para salir): ")
        
        if texto == "-1":
            break

        procesoE = multiprocessing.Process(target=escritor, args=(cola, texto))
        procesoE.start()
        procesoE.join()

        procesoL = multiprocessing.Process(target=lector, args=(cola,))
        procesoL.start()
        procesoL.join()

if __name__ == "__main__":
    main()