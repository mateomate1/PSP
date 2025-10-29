'''
Realizar un programa que
    1. Pide un texto por consola.
    Si el texto es distinto de -1
        · Arranca 2 hilos (escritores) que añaden el texto a una variable global de la siguiente manera
            · El primer hilo añade la mitad del texto
            · El segundo hilo el resto del texto
        · Cuando la escritura ha terminado lanza otro hilo (lector) que lee toda la variable y la presenta en pantalla

Vuelve a pedir el texto y repite el ciclo hasta que el texto introducido ==  “-1”


Se realizarán 3 versiones:
V1 - El hilo principal "Mainthread" controlará que la escritura-lectura se realice ordenadamente.
V2 y V3 - Los hilos que escriben y leen se organizan entre ellos para que el acceso a la variable compartida sea ordenado. Usar 2 tipos distintos de primitivas (Lock y Semaphores, ...)

Se subirán 3 archivos: nombreApellido_com_vX, con X in {1,2,3}
'''
import threading

t = ''

def lector():
    global t
    print(t)

def escritor(texto):
    global t
    t+=texto

def main():
    texto = input('Introduzca un texto o -1 para salir: ')
    while(texto != '-1'):
        t1 = texto[:int(len(texto)/2)+1]
        t2 = texto[-int(len(texto)/2):]
        h1 = threading.Thread(target=escritor, args=(t1,))
        h2 = threading.Thread(target=escritor, args=(t2,))
        h1.start()
        h2.start()
        texto = input('Introduzca un texto o -1 para salir: ')
    lector()


if __name__ == '__main__':
    main()
