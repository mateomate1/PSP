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
    resultado = (base*altura)/2
    figura0.append(resultado)
    print(f'El triangulo de base {base} y altura {altura} tiene un area de {resultado} u^2')
    return resultado

def areaRectangulo(base, altura):
    resultado = (base*altura)
    figura0.append(resultado)
    print(f'El rectangulo de base {base} y altura {altura} tiene un area de {resultado} u^2')
    return resultado

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
    hilof1 = threading.Thread(target=operarFigura, args=(figura1,))
    hilof2 = threading.Thread(target=operarFigura, args=(figura2,))
    hilof3 = threading.Thread(target=operarFigura, args=(figura3,))
    hilof4 = threading.Thread(target=operarFigura, args=(figura4,))

    hilof1.start()
    hilof2.start()
    hilof3.start()
    hilof4.start()

    hilof1.join()
    hilof2.join()
    hilof3.join()
    hilof4.join()

    areaTotal = sum(figura0)
    print(f'El area total es: {areaTotal} u^2')

if __name__ == "__main__":
    main()