import asyncio
import websockets
import json

IP = "192.168.203.205"
PORT = 9000

async def enviar(data):
    uri = "ws://"+IP+":"+str(PORT)
    async with websockets.connect(uri) as websocket:
        mensaje = json.dumps({"palabra":data})
        await websocket.send(mensaje)
        respuesta = await websocket.recv()
        if respuesta == "ok":
            print("Premio enviado correctamente.")
        else:
            print("Error en el envío, reintentando...")
            

def main():
    continuar = True
    while continuar:
        x = input('Introduzca un numero:')
        if(x=="-1"):
            continuar = False
            asyncio.run(enviar("fin"))
        else:
            asyncio.run(enviar(x))


if __name__ == "__main__":
    main()