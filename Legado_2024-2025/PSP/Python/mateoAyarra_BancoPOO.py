'''
Crear en un fichero banco.py con una clase cuenta
1. Clase cuenta
    Datos:
        Nombre del cliente
        Número de cuenta
        Saldo
        Movimientos: Lista de: fecha (string), “tipo de movimiento” (string), cantidad (float).
        Tipo de movimiento será uno de: “apertura”, “ingreso”, “pago”, “cierre”
    
    Métodos:
        Creación del objeto: Parametro de entrada (nombre, fecha)
        Crea un número de cuenta de 10 dígitos usando    str(hash(nombre))[-10:]
        Pone un movimiento inicial de apertura
        ingreso  acepta la cantidad, la suma al saldo y registra el movimiento
        reintegro  acepta la cantidad, la suma al saldo y registra el movimiento
        verSaldo  devuelve el saldo.
        verCliente  devuelve el nombre del cliente.
 
Desde otro fichero importar la clase y hacer una función transferencia que acepta 2 objetos cuenta y mueve dinero de uno a otro.
En el programa main
    Crear 2 clientes.
    Ingresar 10.000 € a cada uno
    Imprimir por pantalla el nombre de cada cliente y el saldo de su cuenta.
    Transferir 4500€ de una cuenta a la otra
    Imprimir por pantalla el nombre de cada cliente y el saldo de su cuenta.

Entrega:
    Fichero banco.py con la clase cuenta
    Fichero alumnoApellido_BOO.py con el resto del código que usa la clase cuenta
'''