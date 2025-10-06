'''
Realizar un programa que pida línea a línea un texto por consola para guardarla en un fichero.

Si la línea es -1 el programa imprime su id de proceso y finaliza
Si la línea es distinta de -1 y -P añade la linea de texto al fichero y vuelve a pedir otra línea
Si la línea es -P el programa arranca un proceso que recibe  el nombre de fichero y tras un retraso de 5 segundos lo imprime en pantalla entre dos líneas de símbolos cualquiera, imprime su PID y termina. Por ejemplo
         ----------
         texto....
         ---------
         process id: 3412

Nota: el retraso puede implementarse con la función sleep de la librería time: time.sleep(5)
'''

import multiprocessing as mp
import time
import os

path = 'texto.txt'
f = open(path, 'r', encoding='UTF-8')

def imprimir():
    time.sleep(5)
    f = open(path, 'r', encoding='UTF-8')
    print('------------------------------')
    print(f.read())
    print('------------------------------')
    f.close()
    print('process id:'+str(os.getppid()))

def main():
    print('Comenzando programa')
    x = input('->')
    while x != '-1':
        if(x == '-p'):
            x = mp.Process(target = imprimir)
            x.start()
        else:
            with open(path, 'a', encoding="UTF-8") as f:
                f.write(x+'\n')
        x = input('->')
    print('process id:'+ str(os.getpid()))

if __name__ == '__main__':
    main()
