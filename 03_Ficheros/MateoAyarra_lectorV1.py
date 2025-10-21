'''
Programa que recorra el texto en el fichero adjunto y mantenga una estructura de datos en la que guardamos cada palabra y el número de veces que aparece.

Construida la estructura, pediremos al usuario una palabra y buscando en esos datos diremos cuántas veces aparece la palabra en el texto.

Al introducir una caracter de fin (-1, fin, etc.) el programa terminara

2ª versión: El programa no distinguirá palabras con o sin tilde. Es decir, "que" y "qué" será lo mismo
'''
import pprint 


diccionario = {}
f = open('texto.txt', 'r', encoding='UTF-8')
contenido = f.read().replace('-','').replace(',','').replace('.','').replace('¿','').replace('?','').replace('¡','').replace('!','')
palabras = contenido.split()
for palabra in palabras:
    palabra = palabra.lower()
    if palabra.lower() not in diccionario:
        diccionario[palabra] = 1
    else:
        diccionario[palabra] += 1

#for clave in diccionario:
#    print(f'{clave} : {diccionario[clave]}')

f.close()

clave = input('Introduce una palabra a buscar(-1 para salir): ').lower()
while clave != '-1':
    if clave in diccionario:
        print(f'La palabra "{clave}" se repite {diccionario[clave]} veces')
    else:
        print(f'La palabra "{clave}" se repite 0 veces')
    clave = input('Introduce una palabra a buscar(-1 para salir): ').lower()
print('Has salido del programa')