numPares = sumaPares = numImpares = 0
productoImpares = 1

for i in range (6):
    n = int(input('Introduce un numero -> '))
    if(n % 2 == 0):
        numPares += 1
        sumaPares += n
    else:
        numImpares += 1
        productoImpares += n
    
if(numImpares == 0):
    productoImpares = 0

print(f'Numero de elementos pares = {numPares} (Suma = {sumaPares}), Numero de elementos impares = {numImpares} (Producto = {productoImpares})')


