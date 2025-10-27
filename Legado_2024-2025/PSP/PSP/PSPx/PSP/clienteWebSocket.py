import asyncio
import websockets
import base64

async def send_file(file_path):
    async with websockets.connect("ws://localhost:8765") as websocket:
        with open(file_path, "rb") as f:
            file_bytes = f.read()
        
        file_data = base64.b64encode(file_bytes).decode()
        await websocket.send(f"{file_path}::{file_data}")
        
        response = await websocket.recv()
        print(response)

async def main():
    await send_file("doc1.pdf")
    await send_file("doc1C.pdf")

asyncio.run(main())
