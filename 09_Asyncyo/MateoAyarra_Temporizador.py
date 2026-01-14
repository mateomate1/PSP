'''
Se pide realizar un temporizador.
El programa pedirá al usuario cuantos segundos desea esperar. El usuario introduce el número y pasados esos segundos el programa sacará por pantalla un mensaje.
Mientras tanto el programa escribirá un punto en pantalla cada 0,5 segundos.
'''
import asyncio

enviado = False

async def saluda(time):
    global enviado
    await asyncio.sleep(time)
    print(f'Ya han pasado {time} segundos')
    enviado = True

async def main():
    message =  asyncio.create_task(saluda(2))
    while not enviado:
        print('.')
        await asyncio.sleep(0.5)

asyncio.run(main())