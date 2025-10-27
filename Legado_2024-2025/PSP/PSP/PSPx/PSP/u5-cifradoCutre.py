import os 

key = "CiudadEscolr"

def creaAlfabeto2(alfabeto, clave):
    newAlf = clave
    for i in range(len(alfabeto)):
        pos = newAlf.find(alfabeto[i])
        if pos == -1:
            newAlf += alfabeto[i]
    print(newAlf)
    return(newAlf)

def encrypt(clave, texto):
    alfabeto = " ABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ,.;:-¿?¡!abcdefghijkalmnñopqrstuvwxyz"
    newA = creaAlfabeto2(alfabeto, clave)
    cifrado = ''
    for i in range(len(texto)):
        pos = alfabeto.find(texto[i])
        cifrado += newA[pos]
    return(cifrado)


def decrypt(clave, texto):
    alfabeto = " ABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ,.;:-¿?¡!abcdefghijkalmnñopqrstuvwxyz"
    newA = creaAlfabeto2(alfabeto, clave)
    dec = ''
    for i in range(len(texto)):
        pos = newA.find(texto[i])
        dec += alfabeto[pos]
    return(dec)


def main():
    cwd = os.path.dirname(os.path.realpath(__file__))
    file = open(cwd + "/" + "ulises.txt","r", encoding="utf-8")
    text = file.read() 
    file.close()
    print(text)
    cf = encrypt(key, text)
    print("-----------------------------------------------------------")
    print(cf)
    print("-----------------------------------------------------------")
    df = decrypt(key, cf)
    print(df)

if __name__ == "__main__":
    main()






