import multiprocessing
import os

def escribir_fichero(nombre_fichero, texto):
    with open(nombre_fichero, 'a') as fichero:
        fichero.write(texto + '\n')
    print(f'Texto escrito: {texto}')

def leer_fichero(nombre_fichero):
    if not os.path.exists(nombre_fichero):
        print('El fichero no existe.')
        return
    with open(nombre_fichero, 'r') as fichero:
        contenido = fichero.read()
    print('Contenido del fichero:\n' + contenido)

def gestionar_proceso(funcion, *args):
    proceso = multiprocessing.Process(target=funcion, args=args)
    proceso.start()
    proceso.join()

def ejecutar():
    nombre_fichero = 'archivo.txt'
    
    while True:
        texto = input('Introduce un texto (-1 para salir): ')
        if texto == '-1':
            print('Programa terminado.')
            break
        
        gestionar_proceso(escribir_fichero, nombre_fichero, texto)
        gestionar_proceso(leer_fichero, nombre_fichero)

if __name__ == '__main__':
    ejecutar()
