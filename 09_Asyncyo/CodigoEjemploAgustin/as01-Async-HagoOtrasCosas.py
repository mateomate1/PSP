import asyncio

async def saluda(delay, mensaje):
    await asyncio.sleep(delay)
    print("SALUDO: -----> {} <----".format(mensaje))

async def main():
    task1 = asyncio.create_task(saluda(2, 'Hello'))
    task2 = asyncio.create_task(saluda(6, 'World'))

    for _ in range(40):
        print("Mientras tanto hago otras cosas")
        await asyncio.sleep(.5)

    await asyncio.Future()  # run forever

asyncio.run(main())