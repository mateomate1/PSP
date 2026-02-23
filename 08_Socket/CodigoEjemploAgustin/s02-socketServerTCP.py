import socket
 
IP = "127.0.0.1"
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.bind((IP, PORT))
  sock.listen()
  conn, addr = sock.accept() # Bloqueante
  with conn:
    print("Cliente desde {} connectado".format(addr[0]))
    while True:
      data = conn.recv(1024) # Bloqueante
      midata = data.decode()
      print (midata) #.decode())  
      if midata == "-1":
        break
      d1 = "Ha llegado "+data.decode()
      d2 = d1.encode()
      conn.send(d2)

