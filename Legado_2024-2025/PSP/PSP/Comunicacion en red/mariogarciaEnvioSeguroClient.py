import asyncio
import websockets
import hashlib
import json

async def enviar_archivos():
    with open("doc1.pdf", "rb") as f:
        doc1 = f.read()
    with open("doc1C.pdf", "rb") as f:
        doc1C = f.read()

    with open("hashfile.txt", "r") as f:
        hash_correcto = f.read().strip()

    archivos = {
        "doc1.pdf": doc1.hex(),    
        "doc1C.pdf": doc1C.hex()
    }

   
    datos = json.dumps({"hash": hash_correcto, "archivos": archivos})

    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(datos)
        print("Archivos enviados.")

asyncio.run(enviar_archivos())
