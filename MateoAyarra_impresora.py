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


f = open('texto.txt', 'r', encoding='UTF-8')
texto = input()
while texto != '-1' and texto !='-p':
    
    texto = input()
