import time

def saluda(delay, mensaje):
    time.sleep(delay)
    print("{} at {}".format(mensaje, time.strftime('%X')))

def main():  
    print("Inicio a las {}".format(time.strftime('%X')))
    saluda(3, 'Hello')
    saluda(1, 'World')
    print("Termino a las {}".format(time.strftime('%X')))

if __name__ == '__main__':
    main()