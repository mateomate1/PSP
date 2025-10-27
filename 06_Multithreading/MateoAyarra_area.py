'''
        _________
      /|<--8m-b4>|
     / |         |
    /  |         |<---6m--->b3
   /   | 12m h1  |__________
  /    |                   |\
 /<10m>|             5m h2 | \
/__b2__|___________________|__\
<------------26 m-------------> b1
'''
import threading

def areaTriangulo(base, altura):
    return (base*altura)/2

def areaRectangulo(base, altura):
    return (base*altura)

def operarFigura(figura):
    forma = figura['forma']
    base = figura['base']
    altura = figura['altura']

    area = 0

    if(forma == 't'):
        area = areaTriangulo(base, altura)
    elif(forma == 'r'):
        area = areaRectangulo(base, altura)
    else:
        print('Figura no soportada')

    return area


#Agrupamos las figuras de izquierda a derecha en un diccionario con las caracteristicas forma, base y altura y por ultimo figura0 que es la figura completa
figura1 = {'forma' : 't', 'base' : 10, 'altura' : 12}
figura2 = {'forma' : 'r', 'base' : 8, 'altura' : 12}
figura3 = {'forma' : 'r', 'base' : 6, 'altura' : 5}
figura4 = {'forma' : 't', 'base' : 26-(10+8+6), 'altura' : 5}
figura0 = []

def main():
    

if __name__ == "__main__":
    main()