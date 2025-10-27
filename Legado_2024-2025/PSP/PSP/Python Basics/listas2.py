n = int(input('Vamos a crear una matriz identidad de n*n, introduzca el valor de n -> '))

matrizIdentidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print("Matriz identidad:")
for x in matrizIdentidad:
    print(x)
