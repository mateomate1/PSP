import threading
import queue

def escritor(nombre, cola):
    while True:
        texto = input(f"{nombre} - Ingresa un texto (-1 para salir): ")
        if texto == "-1":
            cola.put("0x01")
            break
        cola.put(texto)

def lector(cola):
    while True:
        mensaje = cola.get()
        if mensaje == "0x01":
            print("Lector: Codigo de finalizacion recibido. Terminando...")
            break
        print(f"Lector: {mensaje}")

if __name__ == "__main__":
    cola = queue.Queue()

    hilo_escritor1 = threading.Thread(target=escritor, args=("Escritor 1", cola))
    hilo_escritor2 = threading.Thread(target=escritor, args=("Escritor 2", cola))
    hilo_lector = threading.Thread(target=lector, args=(cola,))

    hilo_escritor1.start()
    hilo_escritor2.start()
    hilo_lector.start()

    hilo_escritor1.join()
    hilo_escritor2.join()
    hilo_lector.join()
