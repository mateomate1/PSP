'''
Creación de un API de información deportiva que arranque en la máquina local en el puerto 9000 y que ofrezca los siguientes endpoints

Método: GET. Endpoint: /info - Devuelve un JSON con información del servicio tal como:{"Servicio": "Información deportiva actualizada", "Coste": 20}
Metodo: GET. Endpoint: /primero - Devuelve un JSON con el primer clasificado de la liga:
Metodo: GET: Endpoint: /puntos - Acepta en formato parámetro URL un nombre de Equipo de futbol y devuelve los puntos que lleva en la liga
Metodo: GET: Endpoint: /goles- Acepta en formato query un nombre de Equipo de futbol y devuelve los goles que ha metido en la liga
Método: PUT: Endpoint: /actualiza - Acepta en el formato que desees un nombre de equipo, puntos y goles y actualiza la tabla de la liga

El API llevará autenticación mediante API Key. La clave será "ClavedelAPI"

La tabla de clasificación será esta o algo similar:. Tienes que pensar una estructura de datos para almacenarla..

Equipo                Puntos                  Goles

Bailén                34                         12
Jabalquinto           42                         23
Úbeda                 37                         21
Guarromán             23                         11
'''

from fastapi import FastAPI, Depends, HTTPException, status, Body
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn
import json
import os
import pandas as pd

port = 9000

#API
app = FastAPI()
host = 'localhost'

#Fichero csv a procesar
base = os.path.dirname(__file__)
ruta = os.path.join(base, "liga.csv")

df = pd.read_csv(ruta)

#Metodos para el csv
def addEquipo(nuevaFila):
    df.loc[len(df)] = nuevaFila
    df.to_csv("fichero.csv")

def updateEquipo(nombreEquipo, puntos, goles):
    fila = df[df['Equipo'] == nombreEquipo]
    if not fila.empty:
        df.loc[fila.index, 'Puntos'] = puntos
        df.loc[fila.index, 'Goles'] = goles
        return True
    else:
        return False


@app.get('/info')
def getInfo():
    salida = {}
    salida['Servicio'] = 'Informacion deportiva actualizada'
    salida['Coste'] = 20
    return salida

@app.get('/primero')
def getPrimero():
    return ''

@app.get('/puntos/{nEquipo}')
def getPuntos(nEquipo:str):
    return nEquipo

@app.get('/goles')
def getGoles(nombre:str):
    return nombre

@app.put('/actualiza/{nombreEquipo}')
def updateLiga(nombreEquipo : str, nuevosValores : dict = Body()):
    respuesta = updateEquipo(nombreEquipo, dict['puntos'], dict['goles'])
    if respuesta:
        return {
            'success' : True,
            'message' : "Registro actualizado correctamente",
        }
    else:
        return {
            'success' : False,
            'message' : 'No se encuentra o no existe el equipo buscado'
        }

if __name__ == '__main__':
    uvicorn.run(app, host=host, port=port)