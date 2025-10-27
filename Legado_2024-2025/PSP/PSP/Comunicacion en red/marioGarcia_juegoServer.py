import asyncio
import websockets
import json
import random

num = random.randint(1, 20)
print(f"Número secreto generado: {num}")  # Esto se puede ocultar en producción

async def manejar_conexion(websocket, path):
    global num
    try:
        async for mensaje in websocket:
            datos = json.loads(mensaje)

            if "id" in datos and "apuesta" in datos:
                apuesta = datos["apuesta"]
                id_jugador = datos["id"]

                if apuesta == num:
                    respuesta = {"id": id_jugador, "mensaje": "¡Correcto! Has adivinado el número."}
                    await websocket.send(json.dumps(respuesta))
                    print(f"Jugador {id_jugador} ha adivinado el número. Cerrando servidor...")
                    return  
                else:
                    respuesta = {"id": id_jugador, "mensaje": "Incorrecto, intenta de nuevo."}
                    await websocket.send(json.dumps(respuesta))
                    print(f"Jugador {id_jugador} apostó {apuesta} -> Incorrecto")
            else:
                respuesta = {"error": "Formato inválido"}
                await websocket.send(json.dumps(respuesta))
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado")

async def main():
    async with websockets.serve(manejar_conexion, "localhost", 8765):
        print("Servidor WebSocket iniciado en ws://localhost:8765")
        await asyncio.Future() 

asyncio.run(main())
