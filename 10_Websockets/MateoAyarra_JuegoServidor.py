'''
Realizar un programa que implementa un juego de azar que consiste en adivinar un número del 1 al 20. Para ello, el programa generará el número aleatorio y creará un servidor websocket y admite mensajes con el formato similar al ejemplo:

{"id": 1, "apuesta": 12}

Donde el 'id' identifica al jugador y 'apuesta' el número apostado.

Cuando alguien envia un mensaje le devolverá un mensaje de éxito o fracaso. Cuando alguien acierta el programa termina. 

Se pide:

Realizar el programa descrito (servidor)
Realizar un cliente que envía los datos. Puede pedirlos por teclado.
Probar también a enviar datos desde otros medios. Por ejemplo, la extensión del navegador Chrome llamada Simple WebSocket Client.
Subir el programa realizado como nombreApellido_juegoServer.py y nombreApellido_juegoClient.py
'''
import json
import asyncio
import websockets

def main():
    print

if __name__ == "__main__":
    main()