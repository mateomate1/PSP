l = [7, 12, 3, 19, 0, 8, 14, 6, 11, 15, 2, 20, 4, 18, 9, 10, 1, 5, 13, 17]

media = 0

print(f'Contenido de la lista l: {l}')

media = sum(l) / len(l)

print(f'El valor maximo de los numeros de la lista es {max(l)}')
print(f'La media de los numeros de la lista es {media}')

l.insert(5, 'hola')
l2 = l[6:12]
l3 = l[-4:]

print(f'Contenido de la lista l: {l}')
print(f'Contenido de la lista l2: {l2}')
print(f'Contenido de la lista l3: {l3}')




