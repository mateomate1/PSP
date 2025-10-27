numeros = []
pares,impares = -1,0
sumaP,productoI = 0,1
n = 0

while(n!=-1):
    if(n%2==0):
        pares+=1
        sumaP+=n
    else:
        impares+=1
        productoI*=n
    n=(int(input('Introduce un numero:')))
if(impares==0):
    productoI=0

while(n!=-1):
    n=(int(input('Introduce un numero:')))
    if (n!=-1):
        numeros.append(n)



print('número de elementos par: {} \nSuma: {} \nNumero de elementos impar: {}\n Producto: {}'.format(pares,sumaP,impares,productoI))