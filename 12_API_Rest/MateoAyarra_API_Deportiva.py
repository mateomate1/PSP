'''
Creación de un API de información deportiva que arranque en la máquina local en el puerto 9000 y que ofrezca los siguientes endpoints

Método: GET. Endpoint: /info - Devuelve un JSON con información del servicio tal como:{"Servicio": "Información deportiva actualizada", "Coste": 20}
Metodo: GET. Endpoint: /primero - Devuelve un JSON con el primer clasificado de la liga:
Metodo: GET: Endpoint: /puntos - Acepta en formato parámetro URL un nombre de Equipo de futbol y devuelve los puntos que lleva en la liga
Metodo: GET: Endpoint: /goles- Acepta en formato query un nombre de Equipo de futbol y devuelve los goles que ha metido en la liga
Método PUT: Endpoint:/actualiza - Acepta en el formato que desees un nombre de equipo, puntos y goles y actualiza la tabla de la liga

El API llevará autenticación mediante API Key. La clave será "ClavedelAPI"

La tabla de clasificación será esta o algo similar:. Tienes que pensar una estructura de datos para almacenarla..

Equipo                Puntos                  Goles

Bailén                   34                         12
Jabalquinto           42                         23
Úbeda                   37                         21
Guarromán            23                         11
'''

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials