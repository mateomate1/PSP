import asyncio
import websockets

IP = "10.231.127.29"
PORT = 9000

async def servidorWS(websocket):
    # Se pone a la escucha y recibe una cadena
    cad = await websocket.recv()  
    
    # Gestiona los datos recibidos
    print("Recibido {}".format(cad))
    
    if cad=="-1":
        asyncio.get_event_loop().stop()

async def main():
    async with websockets.serve(servidorWS, IP, PORT):
        await asyncio.Future()  # run forever
        

if __name__ == "__main__":
    asyncio.run(main())



