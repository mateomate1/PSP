'''
Realizar un programa que
Crea una cola
Pide un texto por consola. 
Si el texto es distinto de -1
Arranca 1 proceso (escritor) que añade el texto a las cola termina.
Cuando la escritura ha terminado lanza otro proceso (lector) que lee va leyendo la cola y la saca por pantalla.
Vuelve a pedir el texto y repite el ciclo hasta que el texto introducido ==  “-1”
 
La cola la pasará el padre a los hijos como parámetro.
 
Subir el archivo nombreApellido_procesoCola.py
'''

import multiprocessing

def escritor(cola, texto):
    cola.put(texto)

def lector(cola):
    while not cola.empty():
        print("Lectura de la cola: {}".format(cola.get()))

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
