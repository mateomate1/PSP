import asyncio
import websockets

IP = "10.231.127.29"
PORT = 9000

async def servidorWS(websocket):
    # Se pone a la escucha y recibe una cadena
    cad = await websocket.recv()  
    
    # Gestiona los datos recibidos
    print("Recibido {}".format(cad))
    ack = "Has enviado {}".format(cad)
    
    # Devuelve un valor al cliente (no es obligatorio)
    await websocket.send(ack)
    #print("--> {}".format(ack))

async def otra():
    x=0

async def main():
    server = await websockets.serve(servidorWS, IP, PORT)
    await server.serve_forever()
    #async with websockets.serve(servidorWS, IP, PORT):
    #    await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())



