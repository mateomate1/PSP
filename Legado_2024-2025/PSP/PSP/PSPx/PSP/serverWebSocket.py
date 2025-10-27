import asyncio
import websockets
import hashlib
import base64

AUTH_HASH = "b905aa689d9e0e1bc260b0497effd2ecc95b45f603e4b74f65db149aed01a7df"

async def verify(websocket, path):
    async for message in websocket:
        file_name, file_data = message.split("::")
        file_bytes = base64.b64decode(file_data)
        
        computed_hash = hashlib.sha256(file_bytes).hexdigest()
        if computed_hash == AUTH_HASH:
            await websocket.send(f"Fichero auténtico: {file_name}")

start_server = websockets.serve(verify, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
