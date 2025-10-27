from multiprocessing import Process, Queue
import time
import random

def vigilaHorizonte():
    situacion = ['Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Calma', 'Alarma leve', 'Alarma Media', 'Alarma Grave']
    i = random.randint(0, 9)
    return(situacion[i])

def camara(id, colaAlarmas, colaControl):
    yoSoy = id
    grabando = True
    while grabando:
        sit = vigilaHorizonte()
        if sit != 'Calma':
            alarma = {"Camara": yoSoy, "Alarma": sit}
            colaAlarmas.put(alarma)
        else:
            print("{}:.".format(id))
        if not colaControl.empty():
            orden = colaControl.get()
            if orden["Camara"] != yoSoy:
                colaControl.put(orden)
            else:
                grabando = False
    print("Cerrando cámara {}".format(yoSoy))

def centroControl(colaAlarmas):
    while True:
        alarma = colaAlarmas.get()
        print("ALARMA RECIBIDA: Drone: {} , Nivel {}".format(alarma["Drone"], alarma["Alarma"]))

def main():
    colaA = Queue(maxsize=1000)
    colaC = Queue(maxsize=1000)
    camaras = [0,0,0,0,0]
    activas = 5
    fin = False
    for i in range(5):
        d = Process(target=camara, args=(i, colaA, colaC))
        d.start()
    while not fin:
        alarma = colaA.get()
        print("Camara: {}, {}".format(alarma["Camara"], alarma["Alarma"]))
        camaras[alarma["Camara"]] +=1
        if camaras[alarma["Camara"]] == 4:
            orden = {"Camara": alarma["Camara"]}
            colaC.put(orden)
            activas -= 1
        if (activas==0):
            fin = True

if __name__ == '__main__':
    main()
