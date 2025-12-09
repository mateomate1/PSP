import socket

#Variables
ip = '127.0.0.1'
port = 3000
#Al hacer un mapa podemos definir lo que detecta
conteo = {
    'persona': 0,
    'coche': 0,
    'moto' : 0,
    'bicicleta' : 0
}

sock = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024).decode()
    if data in conteo:
        conteo[data] = conteo[data] + 1
        print(f'Se detecto un(a) {data}, en total se detectaron {conteo[data]}')