import threading

area = 0
lock = threading.Lock()

def areaTriangulo(base, altura):
    suma((base * altura)/2)

def areaRectangulo(base, altura):
    suma(base * altura)

def suma(resultado):
    global area
    global lock
    lock.acquire()
    area += resultado
    lock.release()

def main():
    # Definicion de variables
    baseTriangulo1 = 10
    baseRectangulo1 = 8
    baseRectangulo2 = 6
    baseTotal = 26
    altura1 = 12
    altura2 = 5

    baseTriangulo2 = baseTotal - (baseTriangulo1 + baseRectangulo1 + baseRectangulo2)

    hilo1 = threading.Thread(target=areaTriangulo, args=(baseTriangulo1, altura1))
    hilo2 = threading.Thread(target=areaRectangulo, args=(baseRectangulo1, altura1))
    hilo3 = threading.Thread(target=areaTriangulo, args=(baseTriangulo2,altura2))
    hilo4 = threading.Thread(target=areaRectangulo, args=(baseRectangulo2,altura2))

    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()

    hilo1.join()
    hilo2.join()
    hilo3.join()
    hilo4.join()

    print("Área total del poligono = {}".format(area))


if __name__ == "__main__":
    main()