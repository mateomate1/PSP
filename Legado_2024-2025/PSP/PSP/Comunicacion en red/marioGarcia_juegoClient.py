import asyncio
import websockets
import json

async def jugar():
    async with websockets.connect("ws://localhost:8765") as websocket:
        id_jugador = input("Ingresa tu ID de jugador: ")
        
        while True:
            apuesta = input("Adivina un número del 1 al 20: ")
            
            if not apuesta.isdigit() or not (1 <= int(apuesta) <= 20):
                print("Por favor, ingresa un número válido entre 1 y 20.")
                continue
            
            mensaje = json.dumps({"id": id_jugador, "apuesta": int(apuesta)})
            await websocket.send(mensaje)
            
            respuesta = await websocket.recv()
            datos = json.loads(respuesta)
            
            print(f"Servidor: {datos['mensaje']}")
            
            if "¡Correcto!" in datos["mensaje"]:
                break

asyncio.run(jugar())
