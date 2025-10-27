import asyncio
import websockets

IP = "10.231.127.29"
PORT = 9000

async def clienteWS():
    uri = "ws://"+IP+":"+str(PORT)
    # Conecto al WS
    while True:
        async with websockets.connect(uri) as websocket:
            # Proceso una información y decido enviar al WS
            cad = input("Envío: ")
 
            # Envío la información
            await websocket.send(cad)
            
            # Espero respuesta (opcional)
            devuelto = await websocket.recv()
            print("Recibido: {}".format(devuelto))

asyncio.run(clienteWS())
