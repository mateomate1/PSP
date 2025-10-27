numeros = []
pares,impares = 0,0
sumaP,productoI =0,1

for i in range (0,6):
    n=(int(input('Introduce un numero:')))
    if(n%2==0):
        pares+=1
        sumaP+=n
    else:
        impares+=1
        productoI*=n
if(impares==0):
    productoI=0
print('número de elementos par: {} \nSuma: {} \nNumero de elementos impar: {}\n Producto: {}'.format(pares,sumaP,impares,productoI))