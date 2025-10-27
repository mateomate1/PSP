import socket
import random
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

objetos = ['-', 'persona', 'coche', 'moto', 'bicicleta']

for _ in range(20):  

 obj = random.randint(-10,4)
 if obj <= 0:
    obj = 0
 objetoDetectado = objetos[obj]

 client_socket.sendto(objetoDetectado.encode(), (UDP_IP, UDP_PORT))
 time.sleep(1)
    
client_socket.close()

