import socket
 
UDP_IP = "127.0.0.1"
UDP_PORT = 8080
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    if data.decode() == '-1':
        break
    print("Recibido from {}: {}".format(addr, data.decode()))