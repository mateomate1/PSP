import hashlib

cadena1 = "Hola Mundo Cruel"
cadena2 = "Hola Mundo Cruel!"
cadena_hash = "e11b85c2da6c1c4e8c0c938d9cce1cf7ece7a4a0acf5371cce0eb54da035cc38"

def calcular_hash(cadena):
    return hashlib.sha256(cadena.encode()).hexdigest()
compr1 = calcular_hash(cadena1)
compr2 = calcular_hash(cadena2)

if compr1 == cadena_hash:
    print("El hash corresponde a la cadena 1: ", cadena1)
elif compr2 == cadena_hash:
    print("El hash corresponde a la cadena 2: ", cadena2)
else:
    print("El hash no correspomde a ninguna cadena.")
