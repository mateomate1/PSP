numPares = sumaPares = numImpares = 0
productoImpares = 1

n = int(input('Introduce un numero -> '))

while(n != -1):
    if(n % 2 == 0):
        numPares = numPares + 1
        sumaPares = sumaPares + n
    else:
        numImpares = numImpares + 1
        productoImpares = productoImpares * n
    
    n = int(input('Introduce un numero -> '))

if(numImpares == 0):
    productoImpares = 0

print(f'Numero de elementos pares = {numPares} (Suma = {sumaPares}), Numero de elementos impares = {numImpares} (Producto = {productoImpares})')


