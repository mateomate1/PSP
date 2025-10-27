alumnos = []

with open('alumnos.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        datos = linea.strip().split(', ')  
        alumno = {
            'Nombre': datos[0],
            'Apellido': datos[1],
            'Edad': int(datos[2])
        }
        alumnos.append(alumno)

print("Lista de alumnos:")
for alumno in alumnos:
    print(alumno)
