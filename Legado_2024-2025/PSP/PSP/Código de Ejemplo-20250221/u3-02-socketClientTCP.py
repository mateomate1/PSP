import socket
 
TCP_IP = "127.0.0.1"
TCP_PORT = 5005


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.connect((TCP_IP, TCP_PORT))
  print('Conectado con éxito')
  while True:
    msg = input("Introduce mensaje: ")
    sock.send(msg.encode())
    #numBytes = s.send(msg.encode())
    #print (numBytes) 
    data = sock.recv(1024) #línea bloqueante
    print("Recibido {}, bye".format(data.decode()))
    if msg == '-1':
      break

