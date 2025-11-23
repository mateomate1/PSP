import multiprocessing as mp
import os

def fun():
    print('hola')

def moverse(metros):
    print(f'Te has movido {metros} metros')

def sumar(a, b):
    print(f'{a} + {b} = {a+b}')

x = mp.Process(target=fun) #Si no hay argumentos no se ponen
y = mp.Process(target=moverse, args=(12,)) #Si hay un argumento se pone args=(x,) con , para que no se raye la maquina
z = mp.Process(target=sumar, args=(3,2)) # si hay varios argumentos se pone la lista sin , al final

x.start()
y.start()
z.start()

x.join()
y.join()
z.join()

os.getpid(x) #Process id del proceso x
os.getppid(x) #Process id del proceso padre del proceso x