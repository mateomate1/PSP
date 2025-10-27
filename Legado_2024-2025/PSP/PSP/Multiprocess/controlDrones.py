import random
from multiprocessing import Process, Queue

def vigilaHorizonte():
    situacion = ['Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Alarma leve', 'Alarma Media', 'Alarma Grave']
    return random.choice(situacion)

def dron(idDron, colaAlarmas, colaControl):
    continuar = True
    while continuar:
        alarma = vigilaHorizonte()
        if alarma != 'Calma':
            colaAlarmas.put({'ID': idDron, 'Alarma': alarma})
        if not colaControl.empty():
            orden = colaControl.get()
            if orden == 'Aterrizar':
                continuar = False

def centroControl(colaAlarmas):
    while True:
        while not colaAlarmas.empty():
            alerta = colaAlarmas.get()
            print(f"Centro de control - Alerta recibida: {alerta}")

def main():
    colaAlarmas = Queue()
    colaControl = Queue()
    drones = []
    controlActivo = Process(target=centroControl, args=(colaAlarmas,))
    controlActivo.start()

    orden = input("Escribe una orden (Despegar, Aterrizar, Salir): ").strip().lower()

    while orden != "salir":
        if orden == "despegar":
            idDron = len(drones) + 1
            procesoDron = Process(target=dron, args=(idDron, colaAlarmas, colaControl))
            drones.append(procesoDron)
            procesoDron.start()
            print(f"Dron #{idDron} despegando...")

        elif orden == "aterrizar" and drones:
            colaControl.put("Aterrizar")
            procesoAterrizado = drones.pop(0)
            procesoAterrizado.join()
            print("Aterrizando un dron...")
        else:
            print("Orden no válida o no hay drones disponibles para aterrizar.")
        orden = input("Escribe una orden (Despegar, Aterrizar, Salir): ").strip().lower()

    for procesoDron in drones:
        colaControl.put("Aterrizar")
        procesoDron.join()

    controlActivo.terminate()
    print("Centro de control cerrado.")

if __name__ == "__main__":
    main()
