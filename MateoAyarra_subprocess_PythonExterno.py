import subprocess
import time
import os
import sys

def main():
    error = False
    while not error:
        try:
            subproc = subprocess.Popen(["C:/Users/Alumno/AppData/Local/Programs/Python/Python313/python.exe", "procesoExterno.py"],  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (standardout, standarderr) = subproc.communicate()
            salidaStr = standardout.decode("UTF-8")
            standarderr = standardout.decode("UTF-8")
            print(salidaStr)
            if salidaStr == '7':
                print('Ha salido 7')
                exit()
        except:
            error = True
            salidaStr = "Error en comando"
            print(standarderr)
    


if __name__ == '__main__':
    main()