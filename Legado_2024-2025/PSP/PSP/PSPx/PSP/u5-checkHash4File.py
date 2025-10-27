import hashlib
import os 

cwd = os.path.dirname(os.path.realpath(__file__))
file = open(cwd + "/" + "ulises.txt","r")
text = file.read() # read entire file as bytes
file.close()

hashObject = hashlib.sha256(text.encode())
originalTestDigest = hashObject.hexdigest()

ui = input("Quieres analizar la integridad del fichero (s/n): ")
while ui != 'n':
    file = open(cwd + "/" + "ulises.txt","r")
    text = file.read() # read entire file as bytes
    file.close()
    newHashObject = hashlib.sha256(text.encode())
    newDigest = newHashObject.hexdigest()
    if (originalTestDigest == newDigest):
        print("Fichero inalterado")
    else:
        print("Fichero modificado")
        print(originalTestDigest)
        print(newDigest)
    ui = input("Quieres analizar de nuevo la integridad del fichero (s/n): ")
