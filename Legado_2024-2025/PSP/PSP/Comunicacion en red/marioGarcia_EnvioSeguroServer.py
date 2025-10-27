import asyncio
import websockets
import hashlib
import json

async def recibir_datos(websocket):
    datos = await websocket.recv()
    info = json.loads(datos)
    
    hash_recibido = info["hash"]
    archivos = info["archivos"]

    print("Recibiendo archivos y comparando hashes...")

    for nombre, contenido in archivos.items():
        hash_calculado = hashlib.sha256(contenido.encode()).hexdigest()
        
        if hash_calculado == hash_recibido:
            print(f"✅ El archivo auténtico es: {nombre}")
            return

    print("Ningún archivo coincide con el hash proporcionado.")

async def main():
    async with websockets.serve(recibir_datos, "localhost", 8765):
        print("Servidor WebSocket esperando archivos...")
        await asyncio.Future()

asyncio.run(main())
