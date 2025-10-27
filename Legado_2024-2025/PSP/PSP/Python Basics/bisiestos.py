bisiestos = []

num = int(input('Introduce un anio (-1 para salir) -> '))

while num != -1:
    if(num % 4 == 0 and num % 100 != 0):
        bisiestos.append(num)

    num = int(input('Introduce un anio (-1 para salir) -> '))

print(f'Anios bisiestos', bisiestos)