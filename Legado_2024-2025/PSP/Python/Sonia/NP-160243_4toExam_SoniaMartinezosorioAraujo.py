class Persona():
    def __init__(self, nombre, dni, telefono): 
        self.nombre = str(nombre)
        self.dni = str(dni)
        self.telefono = str(telefono)

    def mostrar_info(self): 
        return f"Informacion personal: \n Nombre: {self.nombre} \n DNI: {self.dni} \n Teléfono: {self.telefono}" 
    def tipificar(self):
        return f"P, Nombre: {self.nombre}, DNI: {self.dni}, Teléfono: {self.telefono}"
    def destipificar(texto):
        datos = texto.strip().split(',')  # por si hay saltos de linea
        if(datos[0] == 'Alumno'):
            return Alumno(datos[1], datos[2], datos[3], datos[4], datos[5])
        elif(datos[0] == 'Profesor'):
            return Profesor(datos[1], datos[2], datos[3], datos[4], datos[5])
        else:
            return Persona(datos[1], datos[2], datos[3])


class Alumno(Persona):
    def __init__(self, nombre, dni, telefono, nivel, clases_recividas):
        super().__init__(nombre, dni, telefono)
        self.nivel = str(nivel)
        self.clases_recividas = str(clases_recividas)

    def mostrar_info(self):
        return f"{super().mostrar_info()} \n Nivel: {self.nivel} \n Clases Recibidas: {self.clases_recividas}"
    def tipificar(self):
        return f'Alumno, Nombre: {self.nombre}, DNI: {self.dni}, Telefono: {self.telefono}, Nivel: {self.nivel}, Clases recividas: {self.clases_recividas}'
    def destipificar(texto):
        datos = texto.split(',')
        return Alumno(datos[1], datos[2], datos[3], datos[4], datos[5])

class Profesor(Persona):
    def __init__(self, nombre, dni, telefono, especialidad, horario):
        super().__init__(nombre, dni, telefono)
        self.especialidad = str(especialidad)
        self.horario = str(horario)
    
    def mostrar_info(self):
        return f"{super().mostrar_info()} \n Especialidad: {self.especialidad} \n Horario: {self.horario}"
    def tipificar(self):
        return f'Profesor, Nombre: {self.nombre}, DNI: {self.dni}, Telefono: {self.telefono}, Especialidad: {self.especialidad}, Horario: {self.horario}'
    def destipificar(texto):
        datos = texto.split(',')
        return Profesor(datos[1], datos[2], datos[3], datos[4], datos[5])

def listarA(): 
    Alum = []
    with open("autoescuelo.txt", "r") as archivo:
        lines = archivo.readlines() #Simpre para leer creo una variable 
        for line in lines:
            Alum.append(Persona.destipificar(line))
        for Alm in Alum:
            print(Alm.mostrar_info())
    return Alum   

def listarP(): 
    Profs = []
    with open("autoescuelo.txt", "r") as archivo:
        lines = archivo.readlines() #Simpre para leer creo una variable 
        for line in lines:
            Profs.append(Persona.destipificar(line))
        for Prof in Profs:
            print(Prof.mostrar_info())
    return Profs   

def sobreescribir(Alum):
    with open("autoescuelo.txt", "w") as archivo: 
        for Alm in Alum:
            archivo.write(f"{Alm.tipificar()} \n")

Alum = []
Profs = []

while True: 
    
    print("Quien eres: \n 1= Alumno \n 2= Profesor")
    Ser = int(input("Indica el número de la opción escogida: "))

    if Ser == 1:

        Alum = listarA()

        print("1. Registrar Alumnono \n 2.Listar Alumnos. \n 3.Actualizar Clases. \n 4.Salir del programa.")
        Opcion = int(input("Indica el número de la opción escogida: "))

        if Opcion == 1: 
            Nom = input("Indica tu nombre: ")
            DNi = input("Indica tu DNI: ")
            Tel = input("Indica tu teléfono: ")
            Nivel = int(input("Indica tu nivel: \n 1.Principiante. \n 2.Intermedio. \n 3.Avanzado. \n Índicalo Aquí: "))
            Num_Cl = int(input("Indica el número de claes realizadas: "))

        
            if Nivel == 1:
                Alm = Alumno(Nom, DNi, Tel, "Nivel Principiante", Num_Cl) 
                Alum.append(Alm)
        
            elif Nivel == 2:
                Alm = Alumno(Nom, DNi, Tel, "Nivel Intermedio", Num_Cl) 
                Alum.append(Alm)

            elif Nivel == 3:
                Alm = Alumno(Nom, DNi, Tel, "Nivel Avanzado", Num_Cl) 
                Alum.append(Alm)
        
            else:
                print("Ese nivel no esta registrado")
        
        elif Opcion == 2:
            for Alm in Alum:
                print(Alm.mostrar_info())
        
        elif Opcion == 3:
            Id = input(print("¿Cuál es tu DNI? :"))
            for i in Alum:
                if i.dni == Id:
                    encontrado = True
                    i.clases_recividas += 1
                    print(f"Ficha actualizada al alumno {i.nombre} {i.dni} \n Clases actalizadas a: {i.clases_recividas}")

                if not encontrado:
                    print ("Su vehiculo no esta listado.")
        
        elif Opcion == 4:
            print("Gracias por usar nuestro programa")
            sobreescribir(Alum) 
            break

    
    if Ser == 2:

        Profs = listarP()

        print("1. Registrar Profesor \n 2.Listar Profesores. \n 3.Salir del programa.")
        Opcions = int(input("Indica el número de la opción escogida: "))

        if Opcions == 1: 
            Nom = input("Indica tu nombre: ")
            DNi = input("Indica tu DNI: ")
            Tel = input("Indica tu teléfono: ")
            Esp = int(input("Indica tu nivel: \n 1.Coche. \n 2.Moto. \n 3.Camión. \n Índicalo Aquí: "))
            Hor = input("Indica tu horario: ")

        
            if Esp == 1:
                Prof = Profesor(Nom, DNi, Tel, "Coche", Hor) 
                Profs.append(Prof)
        
            elif Esp == 2:
                Prof = Profesor(Nom, DNi, Tel, "Moto", Hor) 
                Profs.append(Prof)

            elif Esp == 3:
                Prof = Profesor(Nom, DNi, Tel, "Camión", Hor) 
                Profs.append(Prof)
        
            else:
                print("Esa especialidad no esta registrada")

        elif Opcions == 2:
            for Prof in Profs:
                print(Prof.mostrar_info())
    
        elif Opcion == 3:
            print("Gracias por usar nuestro programa")
            sobreescribir(Profs) 
            break

        
    