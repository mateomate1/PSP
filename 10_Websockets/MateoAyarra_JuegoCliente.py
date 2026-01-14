import asyncio
import websockets
import json

IP = "192.168.202.200"
PORT = "9000"

async def main(apuesta):
    uri = "ws://" + IP + ":" + PORT

    async with websockets.connect(uri) as websocket:
        datos = {
            "id": 1,
            "apuesta": apuesta
        }

        await websocket.send(json.dumps(datos))

        respuesta = await websocket.recv()
        print(respuesta)
        if(respuesta != 'Sigue intentando'):
            print(f'La respuesta correcta era {apuesta}')

for i in range(0, 20, 1):
    asyncio.run(main(i))
