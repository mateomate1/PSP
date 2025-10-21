'''
Slicing: este metodo permite seleccionar partes de una lista usando posiciones e intervalos. Sirve tanto para listas como strings
'''
#        012345 Orden usando el numero en positivo al no usar - no se incluye el valor de la posicion introducida
texto = "Python"
#       -543210 Orden usando el numero en negativo al usar - se incluye el valor de la posicion introducida
print(texto[1:4]) #Devuelve 'yth'
# No incluye los valores de las posiciones limites del slicing
print(texto[:4]) #Devuelve 'Pyth'
print(texto[1:]) #Devuelve 'ython'
print(texto[-5:]) #Devuelve 'ython' lo mismo q [1:]
print(texto[:-4]) #Devuelve 'Py'
print(texto[1:-4]) #Devuelve 'y'
print(texto[1:-3]) #Devuelve 'yt'
#Llegamos a la conclusion que al usar -X invierte el punto desde que empieza a contar los valores
print(texto[::2]) #Devuelve el texto saltando letras de 2 en 2 'Pto', siendo las posiciones 0, 2, 4
print(texto[::-1]) #Al usar un negativo hace lo mismo pero empezando desde el final por lo q 'nohtyP'
#        0123456789
texto = "xxOabcdKef"
#       -0123456789
print(texto[2:9:5]) #Al usar este formato cogera los valores desde la O hasta la f saltando cada 5 letras resultado:OK
