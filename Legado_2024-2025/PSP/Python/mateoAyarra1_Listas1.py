import random

numeros = []
maxnum = 0
media = 0
sublista1 = []
sublista2 = []

for i in range(20):
    numeros.append(random.randint(1,100))

#Hallar el máximo de los números
print(numeros)
print('El numero mayor es '+ str(max(numeros)))
#La media de los números
media/=sum(numeros)/len(numeros)
print('La media de los numeros es '+str(media))
#Insertar la palabra “hola” en la posición 5 e imprimir la lista en pantalla
numeros.insert(5,'hola')
print(numeros)
#Hacer una sublista de las posiciones 6 a la 12
sublista1 = numeros[6:13]
print(sublista1)
#Hacer una sublista con los 4 últimos elementos.
sublista2 = numeros[-4:]
print(sublista2)
