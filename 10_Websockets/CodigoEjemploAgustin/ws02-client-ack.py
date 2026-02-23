import asyncio
import websockets

IP = "127.0.0.1"
PORT = 9000

async def clienteWS():
    uri = "ws://"+IP+":"+str(PORT)
    # Conecto al WS
    cad= ''
    while cad != "-1":
        async with websockets.connect(uri) as websocket:
            # Proceso una información y decido enviar al WS
            cad = input("Qué envío: ")
 
            # Envío la información
            await websocket.send(cad)
            
            # Espero respuesta (opcional)
            devuelto = await websocket.recv()
            print("Ack del servidor: {}".format(devuelto))

asyncio.run(clienteWS())
