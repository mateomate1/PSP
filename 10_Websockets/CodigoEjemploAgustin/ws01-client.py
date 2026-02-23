import asyncio
import websockets

IP = "127.0.0.1"
PORT = 9000

async def clienteWS():
    uri = "ws://"+IP+":"+str(PORT) # ws://127.0.0.1:9000
    cad = ''
    while cad != '-1':
        # Proceso una información y decido enviar al WS
        cad = input("Envío: ")
        # Conecto al WS
        async with websockets.connect(uri) as websocket:
            # Envío la información
            await websocket.send(cad)
            
if __name__ == "__main__":
    asyncio.run(clienteWS())
