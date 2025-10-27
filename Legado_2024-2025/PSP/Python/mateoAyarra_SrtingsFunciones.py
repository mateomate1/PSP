'''
Aceptar varias palabras por teclado hasta un símbolo de final (“-1”, “end”, etc.). 

Usando las funciones siguientes el programa imprimirá la frase compuesta por todas las palabras con la primera letra en mayúscula. 

Además imprimirá cuántas veces aparece en la frase cada una de las vocales.

Hacer las siguientes funciones

-Concatena dos cadenas, separando las palabras por un espacio en blanco y devuelve la cadena concatenada.
-Acepta una cadena y un carácter y devuelve el número de veces que el carácter aparece en la cadena. Si no se incluye carácter devuelve 0.
-Acepta una cadena y convierte la primera letra en mayúscula.
'''
x=''
inn=''
vocals=('a','e','i','o','u')

def concate(a:str, b:str):
    salida=''
    if not a:
        salida = b
    elif not b:
        salida = a
    else :
        salida = a+' '+b
    return (salida)

def contar_caracter(cadena:str, caracter:chr):
    return cadena.count(caracter)

def mayus(c:str):
    mayus = ''
    if c:
        mayus = str(c[0].upper()+c[1:])
    return mayus

while (inn!='EOF'):
    inn = mayus(inn)
    x = concate(x,inn)
    print(x)
    inn=str(input('Introduce la siguiente palabra (EOF para dejar de introducir palabras):'))

print(x)

for i in vocals:
    print('Hay {} \'{}\' en el texto'.format(str(contar_caracter(x,i)),i))
