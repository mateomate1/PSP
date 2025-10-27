import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 9999))
servidor.listen(5)

conteo = {"persona": 0, "coche": 0, "moto": 0, "bicicleta": 0}

try:
    while True:
        conexion, direccion = servidor.accept()
        while True:
            datos = conexion.recv(1024).decode()
            if not datos:
                break
        conexion.close()
except:
    servidor.close()
