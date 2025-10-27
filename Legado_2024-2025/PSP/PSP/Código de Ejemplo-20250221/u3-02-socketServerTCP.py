import socket
 
TDP_IP = "127.0.0.1"
TDP_PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.bind((TDP_IP, TDP_PORT))
  sock.listen()
  conn, addr = sock.accept() # Bloqueante
  with conn:
    print("Cliente desde {} connectado".format(addr[0]))
    while True:
      data = conn.recv(1024) # Bloqueante
      print (data.decode())  
      if data == b"-1":
        break
      conn.sendall(("Ha llegado "+data.decode()).encode())

