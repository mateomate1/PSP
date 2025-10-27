import hashlib
import os 

cwd = os.path.dirname(os.path.realpath(__file__))

fileA = input("Introduce nombre de fichero A: ")
fileB = input("Indroduce nombre de fichero B: ")

fA = open(cwd + "/" + fileA,"rb")
fAb = fA.read() # read entire file as bytes

hashObject = hashlib.sha256(fAb)
hashA = hashObject.hexdigest()
print("fichero A: ", hashA)

fB = open(cwd + "/" + fileB,"rb")
fBb = fB.read() # read entire file as bytes

hashObject = hashlib.sha256(fBb)
hashB = hashObject.hexdigest()
print("fichero B: ", hashB)
