'''
Hacer un programa que usando la libreria subprocess lance el intérprete de Python para ejecutar el código adjunto. Cuando el programa hijo devuelva un 7 el programa padre debe terminar.

NOTA: El código adjunto devuelve un número aleatorio.
'''

import subprocess

while True:
    process = subprocess.Popen(['python', 'procesoExterno.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, errorout = process.communicate()
    
    num = int(out.decode().strip())
    
    print(num)
    
    if num == 7:
        break