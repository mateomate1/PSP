'''
Se pide hacer un programa que lea el fichero adjunto y construya una lista de estructuras dict que luego presentará en pantalla.

Cada estructura dict será del tipo {'Nombre':'Ana', 'Apellido': 'Gil', 'Edad': 21}
'''

personas = []

with open('alumnos.txt','r', encoding='utf-8') as file: #Si no se usa el encoding los nombres con tildes o ñ son ilegibles
    lineas = file.readlines()

for linea in lineas:
    
    datos = linea.strip().split(',') #strip para eliminar el salto de linea

    if len(datos) != 3:
        continue #Esto nos asegura que si entra una entrada con un numero diferente de datos a los pedidos la ignora

    nombre, apellido, edad = datos
    
    persona = {
        'nombre':nombre,
        'apellido':apellido,
        'edad':edad
    }
    personas.append(persona)

for i in personas:
    print(i)