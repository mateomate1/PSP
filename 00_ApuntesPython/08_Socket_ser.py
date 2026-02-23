import socket

#TCP

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 5000))
servidor.listen(1)

print("Esperando conexion...")

cliente, direccion = servidor.accept()
print("Conectado con " + str(direccion))

datos = cliente.recv(1024)
print("Mensaje recibido: " + datos.decode())

cliente.send("Hola cliente".encode())

cliente.close()
servidor.close()