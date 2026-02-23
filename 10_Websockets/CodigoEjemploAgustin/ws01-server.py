import asyncio
import websockets

IP = "127.0.0.1"
PORT = 9000

async def servidorWS(websocket):
    # Se pone a la escucha y recibe una cadena
    cad = await websocket.recv()  
    # Gestiona los datos recibidos
    print("Recibido {}".format(cad))
    if cad == '-1':
        exit()


async def main():
    async with websockets.serve(servidorWS, IP, PORT):
        print("Activo Servidor WS")
        await asyncio.Future()  # run forever
        

if __name__ == "__main__":
    asyncio.run(main())



