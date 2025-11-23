x = ''

def write():
    with open('fichero.txt', 'r', encoding = 'utf-8') as f: #Metodo 1 para abrir ficheros, se cierra automaticamente
        texto = f.read() #Esto lee el teto entero en una sola variable
        linea = f.readline() #Lee lineas hasta que no haya mas y devuelve null
        while linea:
            texto += linea
            linea = f.readline()

def read():
    f = open('fichero.txt', 'w', encoding='utf-8')
    s = 'texto'
    f.write(s)
    f.close() #Asegurarse de cerrar para no gastar recursos