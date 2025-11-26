import subprocess
import multiprocessing as mp
import time

def crearFichero(fichero):
    f = open(fichero, 'w', encoding='UTF-8')
    f.write('')


def leerFichero(fichero, clave):
    while(True):
        time.sleep(2)
        with open(fichero, 'r', encoding = 'utf-8') as f:
            linea = f.readline()
            while(linea):
                linea = f.readline()
                print(linea)
                palabras = linea.split(' ')
                for palabra in palabras:
                    if(palabra == clave):
                        print(f'Se ha encontrado la palabra {clave}')

def lanzarNotepad(fichero):
    subproc = subprocess.Popen(['notepad.exe', fichero])

def main():
    fichero = input('Introduce el nombre del fichero: ')
    fichero = fichero+'.txt'
    crearFichero(fichero)
    clave = input('Introduce la palabra clave: ')

    p1 = mp.Process(target=lanzarNotepad, args=(fichero,))
    p2 = mp.Process(target=leerFichero, args=(fichero, clave))

    p1.start()
    p2.start()



if __name__ == '__main__':
    main()