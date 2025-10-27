import threading
import queue
import random
import time

# Modelos de coches con precios
MODELOS = [
    {"modelo": "Golf", "precio": 23000},
    {"modelo": "Passat", "precio": 27000},
    {"modelo": "Polo", "precio": 19000},
    {"modelo": "Tiguan", "precio": 32000},
]

# Cola de producción
cola_coches = queue.Queue()

def linea_produccion(id_linea, n_coches):
    """Función para simular la línea de producción."""
    for _ in range(n_coches):
        coche = random.choice(MODELOS)
        cola_coches.put(coche)
        print(f"Línea {id_linea} ha fabricado: {coche['modelo']} por {coche['precio']}€")
        time.sleep(random.uniform(0.1, 0.5))  # Simula tiempo de producción
    print(f"Línea {id_linea} ha terminado de fabricar coches.")

def concesionario(id_concesionario):
    """Función para simular el concesionario."""
    while True:
        try:
            coche = cola_coches.get(timeout=3)  # Espera 3 segundos por un coche
            print(f"Concesionario {id_concesionario} ha vendido: {coche['modelo']} por {coche['precio']}€")
        except queue.Empty:
            print(f"Concesionario {id_concesionario}: No hay coches disponibles.")
            break

def main():
    """Función principal para iniciar el programa."""
    # Pedir al usuario los números de líneas de producción y concesionarios
    num_lineas = int(input("¿Cuántas líneas de producción quieres arrancar? "))
    num_concesionarios = int(input("¿Cuántos concesionarios quieres arrancar? "))
    coches_por_linea = 50

    # Crear hilos de líneas de producción
    lineas = [
        threading.Thread(target=linea_produccion, args=(i + 1, coches_por_linea))
        for i in range(num_lineas)
    ]

    # Crear hilos de concesionarios
    concesionarios = [
        threading.Thread(target=concesionario, args=(i + 1))
        for i in range(num_concesionarios)
    ]

    # Iniciar hilos de líneas de producción
    for linea in lineas:
        linea.start()

    # Iniciar hilos de concesionarios
    for concesionario_hilo in concesionarios:
        concesionario_hilo.start()

    # Esperar a que todos los hilos de líneas de producción terminen
    for linea in lineas:
        linea.join()

    # Esperar a que todos los hilos de concesionarios terminen
    for concesionario_hilo in concesionarios:
        concesionario_hilo.join()

    print("Producción y ventas finalizadas.")

if __name__ == "__main__":
    main()
