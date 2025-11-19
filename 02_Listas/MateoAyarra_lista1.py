'''
Crear una lista con 20 números y sobre ella:

Hallar el máximo de los números
La media de los números
Insertar la palabra “hola” en la posición 5 e imprimir la lista en pantalla
Hacer una sublista de las posiciones 6 a la 12
Hacer una sublista con los 4 últimos elementos.
Incluir el código en el fichero nombreApellido1_Listas1.py y subir a este espacio
'''
import random as rd

lista = []

for i in range(20):
    lista.append(rd.randint(0,100))
print(lista)
#Hallar el máximo de los números
lista.sort()
print(f'El mayor de los numeros en la lista es: {max(lista)}')

#La media de los números
print(f'La media de los numeros en la lista es: {sum(lista)/len(lista)}')

#Insertar la palabra “hola” en la posición 5 e imprimir la lista en pantalla
lista.insert(4,'hola')
print(lista)

#Hacer una sublista de las posiciones 6 a la 12
print(lista[5:12])

#Hacer una sublista con los 4 últimos elementos.
print(lista[-4:])