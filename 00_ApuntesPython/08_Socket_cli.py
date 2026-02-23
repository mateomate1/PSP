import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 5000))

cliente.send("Hola servidor".encode())

respuesta = cliente.recv(1024)
print("Respuesta: " + respuesta.decode())

cliente.close()