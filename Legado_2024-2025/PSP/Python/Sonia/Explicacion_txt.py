'''
Necesitamos lo metodos para gestionar el txt, sin embargo podemos priscindir de la lista y usar solo listas temporales para tareas especificas
'''
class Vehiculo():
    def __init__(self, marca, modelo, ano, km): 
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano
        self.km = int(km)

    def mostrar_info(self): 
        return f"Informacion de su vehiculo: \n Marca: {self.marca} \n Modelo: {self.modelo} \n Kilometraje: {self.km}km \n Ano: {self.ano}" 
    def tipificar(self):
        return f'V,{self.marca},{self.modelo},{self.ano},{self.km}' # Esto devuelve texto
    def destipificar(texto):
        datos = texto.strip().split(',')  # por si hay saltos de linea
        if(datos[0] == 'C'):
            return Camion(datos[1], datos[2], datos[3], datos[4], datos[5])
        elif(datos[0] == 'F'):
            return Furgoneta(datos[1], datos[2], datos[3], datos[4], datos[5])
        elif(datos[0] == 'M'):
            return Motocicleta(datos[1], datos[2], datos[3], datos[4], datos[5])
        else:
            return Vehiculo(datos[1], datos[2], datos[3], datos[4])
    
class Camion(Vehiculo):
    def __init__(self, marca, modelo, ano, km, capacidad_carga):
        super().__init__(marca, modelo, ano, km)
        self.capacidad_carga = capacidad_carga

    def mostrar_info(self):
        return f"{super().mostrar_info()} \n Capacidad de carga: {self.capacidad_carga}"
    def tipificar(self):
        return f'C,{self.marca},{self.modelo},{self.ano},{self.km},{self.capacidad_carga}'
    def destipificar(texto):
        datos = texto.split(',')
        return Camion(datos[1], datos[2], datos[3], datos[4], datos[5])
    
class Furgoneta(Vehiculo):
    def __init__(self, marca, modelo, ano, km, capacidad_pasajeros):
        super().__init__(marca, modelo, ano, km)
        self.capacidad_pasajeros = capacidad_pasajeros

    def mostrar_info(self):
        return f"{super().mostrar_info()} \n Capacidad de pasajeros: {self.capacidad_pasajeros}"
    def tipificar(self):
        return f'F,{self.marca},{self.modelo},{self.ano},{self.km},{self.capacidad_pasajeros}'
    def destipificar(texto):
        datos = texto.split(',')
        return Furgoneta(datos[1], datos[2], datos[3], datos[4], datos[5])
    
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, ano, km, tipo):
        super().__init__(marca, modelo, ano, km)
        self.tipo = tipo

    def mostrar_info(self):
        return f"{super().mostrar_info()} \n Tipo: {self.tipo}"
    def tipificar(self):
        return f'M,{self.marca},{self.modelo},{self.ano},{self.km},{self.tipo}'
    def destipificar(texto):
        datos = texto.split(',')
        return Motocicleta(datos[1], datos[2], datos[3], datos[4], datos[5])


#Métodos del programa.
def registrar(datos): #Debe de llamarse diferente lo que va entre paréntesis
    with open("vehiculos.txt", "a") as archivo:
        archivo.write(f"{datos.tipificar()} \n")#El . es para llamar al metodo o atributo

def listar(): #Si no añado nada dejo el paréntesis vacio
    vehiculos = []
    with open("vehiculos.txt", "r") as archivo:
        lines = archivo.readlines() #Simpre para leer creo una variable 
        for line in lines:
            vehiculos.append(Vehiculo.destipificar(line))
        for vehiculo in vehiculos:
            print(vehiculo.mostrar_info())
    return vehiculos    

def sobreescribir(Vh):
    with open("vehiculos.txt", "w") as archivo: #W sobreescribe el archivo
        for vehiculo in Vh: #Recorremos la lista de vehiculos que le pasamos al metodo, esta lista ya esta cambiada lo que necesitamos por lo que se añade entera eliminando lo que hubiera en el archivo txt
            archivo.write(f"{vehiculo.tipificar()} \n")# No olvidar \n para que cada vehiculo salga simbolice una linea, pues cada iteracion del for es un vehiculo

#Lista de los vehículos.
encontrado = False

while True: 
    print(" 1. Registrar un vehículo \n 2.Listar los vehículos registrados. \n 3.Actualizar el kilometraje de un vehículo. \n 4.Eliminar un vehículo de la lista. \n 5.Salir del programa.")
    
    opcion = int(input("Indica el número de la opción escogida: "))

    if opcion == 1:
        Clase = int(input("Indica tu tipo de vehículo: \n 1.Camión. \n 2.Furgoneta. \n 3.Motocicleta. \n Cual de esos tres vehúculos es su vehículo: "))
        
        Mc = input("Indica la marca: ")
        Md = input("Indica el modelo: ")
        An = int(input("Indica el año: "))
        Kim = int(input("Indica el kilometraje: "))
    
        if Clase == 1:
            Cc = input("Indica la capacidad de carga: ")
            vehiculo = Camion(Mc, Md, An, Kim, Cc) #Las clase se debe de escribir igual que en la clase hija porque asi hemos diseñado el constructor de la clase hija
            registrar(vehiculo)
        
        elif Clase == 2:
            Cp = input("Indica la capacidad de pasajeros: ")
            vehiculo = Furgoneta(Mc, Md, An, Kim, Cp)
            registrar(vehiculo)

        elif Clase == 3:
            Tp = input("Indica el tipo de motocicleta: ")
            vehiculo = Motocicleta(Mc, Md, An, Kim,Tp)
            registrar(vehiculo) #Escribir en TxT
        
        else:
            print("Ese vehiculo no se puede registrar")
    
    elif opcion == 2:
        listar() #Listar TxT
    
    elif opcion == 3:
        Umc = input("¿Cual es la marca de tu coche?:" )
        vehiculos = listar() #Variable temporal para listar los vehiculos recuperados del txt
        for i in vehiculos:
            if i.marca == Umc:
                encontrado = True
                i.km += 500
                #break si dejamos el break solo nos cambia el prier vehiculo que encuentre de esa marca
        if encontrado: #Encontrado es una variable booleana(que solo coge 2 valores True/False) que se utiliza para saber si el vehiculo se ha encontrado o no
            sobreescribir(vehiculos)#Sobreescribimos al final para que no sobreescriba el archivo mas veces de las necesarias

        if not encontrado:
            print ("Su vehiculo no esta listado.")

        encontrado = False #Reiniciamos la variable, fuera del bucle y despues de el if.
    
    elif opcion == 4:
        Umc = input("¿Cual es la marca de tu coche?:" )
        vehiculos = listar()
        for i in vehiculos:
            if i.marca == Umc:
                encontrado = True
                vehiculos.remove(i)
                print(f"Vehiculo {i.marca} {i.modelo} eliminado con exito")
                #break si dejamos el break solo elimina la primera coincidencia
        if encontrado:
            sobreescribir(vehiculos) #Editar TxT
        if not encontrado:
            print ("Su vehiculo no esta listado.")
        
        encontrado = False #Reiniciamos la variable, fuera del bucle y despues de el if.
    
    elif opcion == 5:
        print ("Gracias por usar nuestro programa")
        break

    else:
        print ("Esa opción no es válida")