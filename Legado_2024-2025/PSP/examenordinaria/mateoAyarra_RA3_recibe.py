import asyncio
import websockets
import json

IP = "192.168.203.205"
PORT = 8080

texto = []

async def recibir_premio(websocket, path):
    async for mensaje in websocket:
        data = json.loads(mensaje)
        texto.append(data['mensaje'])
        print('Texto recibido')
        if(data['mensaje'] == 'fin'):
            for t in texto:
                print(t+' ')

async def main():
    server = await websockets.serve(recibir_premio, IP, PORT)
    async with websockets.serve():
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())

