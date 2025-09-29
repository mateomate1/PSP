'''
Programa que recorra el texto en el fichero adjunto y mantenga una estructura de datos en la que guardamos cada palabra y el número de veces que aparece.

Construida la estructura, pediremos al usuario una palabra y buscando en esos datos diremos cuántas veces aparece la palabra en el texto.

Al introducir una caracter de fin (-1, fin, etc.) el programa terminara

2ª versión: El programa no distinguirá palabras con o sin tilde. Es decir, "que" y "qué" será lo mismo
'''
import pprint 

diccionario = {}
f = open('texto.txt', 'r', encoding='UTF-8')
contenido = f.read().replace('-','').replace(',','').replace('.','').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
palabras = contenido.split('')
for palabra in palabras:
    palabra = palabra.lower()
    print(palabra)
    if palabra.lower() not in diccionario:
        diccionario[palabra] = 1
    else:
        diccionario[palabra] += 1

f.close()

clave = input('Introduce una palabra a buscar(-1 para salir)')
