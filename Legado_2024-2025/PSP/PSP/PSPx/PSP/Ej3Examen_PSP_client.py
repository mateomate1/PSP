import asyncio
import websockets
import json

IP = "192.168.203.205"
PORT = 9000

async def enviar_premio():
    uri = "ws://"+IP+":"+str(PORT)
    async with websockets.connect(uri) as websocket:
        while True:
            categoria = input("Introduce la categoría del premio. Para terminar, escriba 'fin': ")
            if categoria.lower() == "fin":
                mensaje = json.dumps({"categoria": "fin", "premio": ""})
                await websocket.send(mensaje)
                respuesta = await websocket.recv()
                print("Respuesta del servidor:", respuesta)
                break

            premio = input("Introduce el ganador del premio: ")
            mensaje = json.dumps({"categoria": categoria, "premio": premio})
            await websocket.send(mensaje)
            respuesta = await websocket.recv()

            if respuesta == "ok":
                print("Premio enviado correctamente.")
            else:
                print("Error en el envío, reintentando...")

asyncio.run(enviar_premio())
