import asyncio
import websockets

connected_websockets = list()

IP = "10.231.127.29"
PORT = 9000

async def servidorBC(ws):
    global connected_websockets
    connected_websockets.append(ws)

    cad = await ws.recv()  
    if cad != '0':
        print("Recibido {}".format(cad))
        ack = "Hola a todos, me ha llegado {}".format(cad)

        websockets.broadcast(connected_websockets, ack)
        print("Enviado a todos {}".format(cad))


async def main():
    print("{} - {}".format(IP,PORT))
    async with websockets.serve(servidorBC, IP, PORT):
        await asyncio.Future()  # run forever

asyncio.run(main())


