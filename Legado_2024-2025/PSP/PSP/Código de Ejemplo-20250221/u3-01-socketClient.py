import socket
 
UDP_IP = "127.0.0.1"
UDP_PORT = 8080
 
print("UDP IP: {}".format(UDP_IP))
print("UDP puerto: {}".format(UDP_PORT))

while True:
    msg = input("Introduce mensaje: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    if msg == '-1':
        break
