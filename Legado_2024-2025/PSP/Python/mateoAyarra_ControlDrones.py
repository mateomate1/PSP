import multiprocessing
import random
import time

def vigilaHorizonte():
    situacion = ['Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Alarma leve', 'Alarma Media', 'Alarma Grave']
    return random.choice(situacion)

def dron_proceso(dron_id, cola_alarmas, cola_control):
    print(f"Dron {dron_id} en espera de órdenes...")
    while True:
        situacion = vigilaHorizonte()
        if situacion != "Calma":
            alarma = {'dron_id': dron_id, 'situacion': situacion}
            cola_alarmas.put(alarma)
            print(f"Dron {dron_id} reporta: {situacion}")
        if not cola_control.empty():
            orden = cola_control.get()
            if orden == "Aterrizar":
                print(f"Dron {dron_id} ha recibido orden de aterrizar.")
                break
        time.sleep(random.uniform(1, 3))

def centro_control_proceso(cola_alarmas):
    print("Centro de control activado.")
    while True:
        if not cola_alarmas.empty():
            alarma = cola_alarmas.get()
            print(f"ALERTA: Dron {alarma['dron_id']} reporta {alarma['situacion']}")
        time.sleep(0.5)

def main():
    cola_alarmas = multiprocessing.Queue()
    cola_control = multiprocessing.Queue()
    proceso_centro = multiprocessing.Process(target=centro_control_proceso, args=(cola_alarmas,))
    proceso_centro.start()
    procesos_drones = []

    while True:
        orden = input("Ingrese orden (Despegar/Aterrizar/Salir): ").strip().lower()
        if orden == "despegar":
            dron_id = len(procesos_drones) + 1
            proceso_dron = multiprocessing.Process(target=dron_proceso, args=(dron_id, cola_alarmas, cola_control))
            procesos_drones.append(proceso_dron)
            proceso_dron.start()
            print(f"Dron {dron_id} ha despegado.")
        elif orden == "aterrizar":
            if procesos_drones:
                cola_control.put("Aterrizar")
                proceso_terminado = procesos_drones.pop(0)
                proceso_terminado.join()
                print("Un dron ha aterrizado.")
            else:
                print("No hay drones activos para aterrizar.")
        elif orden == "salir":
            print("Cerrando centro de control y aterrizando todos los drones.")
            for proceso_dron in procesos_drones:
                cola_control.put("Aterrizar")
                proceso_dron.join()
            proceso_centro.terminate()
            proceso_centro.join()
            break
        else:
            print("Orden no reconocida.")

if __name__ == "__main__":
    main()
