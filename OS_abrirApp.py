import os
#os.execvp recibe (file, args[]) args[0] es el nombre del programa, el resto son argumentos
os.execvp('notepad.exe', ['notepad.exe', 'C:/Users/Alumno/Desktop/DAM 2.2/PSP/texto.txt'])
