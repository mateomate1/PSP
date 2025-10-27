import asyncio
import websockets
import json

IP = "192.168.203.205"
PORT = 9000
premios = []

async def recibir_premio(websocket, path):
    async for mensaje in websocket:
        data = json.loads(mensaje)
        if "categoria" in data and "premio" in data:
            if data["categoria"] == "fin":
                print("Recepción finalizada. Lista de premios:")
                for p in premios:
                    print(p)
                return
            premios.append(data)
            print("Premios hasta ahora:", premios)

async def main():
    server = await websockets.serve(recibir_premio, IP, PORT)
    async with websockets.serve():
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())

