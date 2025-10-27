import threading

def areaTriangulo(base, altura, resultado, i):
    area = (base * altura) / 2
    resultado[i] = area

def areaRectangulo(base, altura, resultado, i):
    area = base * altura
    resultado[i] = area

def main():
    resultado = [0, 0, 0, 0]

    hiloTriangulo = threading.Thread(target=areaTriangulo, args=(10,12,resultado,0))
    hiloTriangulo2 = threading.Thread(target=areaTriangulo, args=(5,2,resultado,1))
    hiloRectangulo = threading.Thread(target=areaRectangulo, args=(8,12,resultado,2))
    hiloRectangulo2 = threading.Thread(target=areaRectangulo, args=(6,5,resultado,3))
   
    hiloTriangulo.start()
    hiloTriangulo2.start()
    hiloRectangulo.start()
    hiloRectangulo2.start()

    hiloTriangulo.join()
    hiloTriangulo2.join()
    hiloRectangulo.join()
    hiloRectangulo2.join()

    areaTotal = sum(resultado)

    print(f"El area total es: {areaTotal} u^2")

if __name__ == "__main__":
    main()