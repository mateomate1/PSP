class Vehiculo():
    def __init__(self, marca, modelo, ano, km): 
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano
        self.km = int(km)

    def mostrar_info(self): 
        return f"Informacion de su vehículo: \n Marca: {self.marca} \n Modelo: {self.modelo} \n Kilometraje: {self.km}km \n Año: {self.ano}" 

    
class Camion(Vehiculo):
    def __init__(self, marca, modelo, ano, km, capacidad_carga):
        super().__init__(marca, modelo, ano, km)
        self.capacidad_carga = capacidad_carga

    def mostrar_info(self):
        return f"{super().mostrar_info()} \n Capacidad de carga: {self.capacidad_carga}"
    
class Furgoneta(Vehiculo):
    def __init__(self, marca, modelo, ano, km, capacidad_pasajeros):
        super().__init__(marca, modelo, ano, km)
        self.capacidad_pasajeros = capacidad_pasajeros

    def mostrar_info(self):
        return f"{super().mostrar_info()} \n Capacidad de pasajeros: {self.capacidad_pasajeros}"
    
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, ano, km, tipo):
        super().__init__(marca, modelo, ano, km)
        self.tipo = tipo

    def mostrar_info(self):
        return f"{super().mostrar_info()} \n Tipo: {self.tipo}"

#Métodos del programa.
def registrar(datos): #Debe de llamarse diferente lo que va entre paréntesis
    with open("vehiculos.txt", "a") as archivo:
        archivo.write(f"{datos} \n")

def listar(): #Si no añado nada dejo el paréntesis vacio
    with open("vehiculos.txt", "r") as archivo:
        Cont = archivo.read() #Simpre para leer creo una variable 
        print(Cont)

def sobreescribir(Vh):
    with open("vehiculos.txt", "w") as archivo:
        archivo.write (f"{Vh} \n")

#Lista de los vehículos.
Vh = []
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
            vehiculo = Camion(Mc, Md, An, Kim, Cc) #Las clase se debe de escribir igual que en la clase hija
            Vh.append(vehiculo) #Nombre de la lista.append(registrado)
            registrar(Vh)
        
        elif Clase == 2:
            Cp = input("Indica la capacidad de pasajeros: ")
            vehiculo = Furgoneta(Mc, Md, An, Kim, Cp)
            Vh.append(vehiculo)
            registrar(Vh)

        elif Clase == 3:
            Tp = input("Indica el tipo de motocicleta: ")
            vehiculo = Motocicleta(Mc, Md, An, Kim,Tp)
            Vh.append(vehiculo)
            registrar(Vh) #Escribir en TxT
        
        else:
            print("Ese vehiculo no se puede registrar")
    
    elif opcion == 2:
        for vehiculo in Vh:
            tipo = vehiculo.__class__.__name__

            print(vehiculo.mostrar_info())
        listar() #Listar TxT
    
    elif opcion == 3:
        Umc = input("¿Cual es la marca de tu coche?:" )

        for i in Vh:
            if i.marca == Umc:
                encontrado = True
                i.km += 500
                print(f"Matenimiento realizado a {i.marca} {i.modelo} \n Kilometraje actualizado: {i.km}")
                sobreescribir(Vh) #Editar TxT
                break

        if not encontrado:
            print ("Su vehiculo no esta listado.")
        
        encontrado = False #Reiniciamos la variable, fuera del bucle y despues de el if.
    
    elif opcion == 4:
        Umc = input("¿Cual es la marca de tu coche?:" )

        for i in Vh:
            if i.marca == Umc:
                encontrado = True
                Vh.remove(i)
                print(f"Vehiculo {i.marca} {i.modelo} eliminado con exito")
                sobreescribir(Vh) #Editar TxT
                break

        if not encontrado:
            print ("Su vehiculo no esta listado.")
        
        encontrado = False #Reiniciamos la variable, fuera del bucle y despues de el if.
    
    elif opcion == 5:
        print ("Gracias por usar nuestro programa")
        break
    
    else:
        print ("Esa opción no es válida")

def main():
    print('Hellow')