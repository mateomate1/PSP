'''
Necesitamos elaborar un API que ofrezca el pronóstico del tiempo de las 6 próximas horas para todos los municipios de España.

El API se implementará como método GET al que se le pasará como parámetro el nombre del municipio y devolverá una estructura JSON conteniendo:

Nombre del Municipio
Provincia
Para cada una de las 6 horas siguientes:
Estado del cielo
Temperatura
Precipitación
Dirección del viento
Velocidad del viento
VERSIÓN 2: Añadiremos un sistema de log mediante el que se generará un fichero de log en el que registrará cada llamada que reciba y un sello de tiempo en un formato

Llamada API: <timestamp>
Llamada API: <timestamp>
....

Pistas:

Hay que averiguar cómo funciona el API de AEMET. Para eso tenéis que usar Postman. Tendréis que saber cómo llamar, conseguir el api_key, analizar lo que devuelve, etc.
Necesitareis analizar las diferentes llamadas de predicción por municipio para seleccionar la que devuelve por horas.
Tenéis que llamar con el código de municipio que está en los ficheros adjuntos (contienen la misma información pero en diferente formato). El código de municipio es la concatenación de las columas CPRO y CMUN pero CMUN. Habrá que buscar el código en los ficheros.
Con lo que devuelva AEMET se construye el formato pedido y se devuelve.
'''

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import requests
import json
import os
import pandas as pd
import uvicorn

#Api a procesar
BASE = 'https://opendata.aemet.es/opendata'
endpoint = '/api/prediccion/especifica/municipio/diaria/'

key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtYXRlb2F5YXJyYWJhcmJlcm9AZ21haWwuY29tIiwianRpIjoiZGE5MmRiZmEtMGFlNy00MzNiLTg0NDAtMDc2MmIyYTYwNDkwIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3NzAwMzU3MTEsInVzZXJJZCI6ImRhOTJkYmZhLTBhZTctNDMzYi04NDQwLTA3NjJiMmE2MDQ5MCIsInJvbGUiOiIifQ.A4szG1CuWFevrxM1SnR_cHLkvJ5-tdPqdD8eqcQWUaQ'

authString = {"api_key": key}

#Fichero csv a procesar
base = os.path.dirname(__file__)
ruta = os.path.join(base, "20codmun.csv")

df = pd.read_csv(ruta)

#Api de salida
app = FastAPI()


def preguntar(entrada):
    lista = buscar(entrada)
    salida = {}
    if lista.empty:
        lista = listar(entrada)
        salida["Error"] = 'No se encontraron coincidencias'
        sugerencias = []
        if len(lista) != 0:
            salida["Posibles valores"] = {}
            nombres = lista["NOMBRE"].unique().tolist()
            for i in nombres:
                sugerencias.append(i)
        salida["sugerencias"] = sugerencias
    else:
        cp = get(lista.iloc[0])
        datos = recogerTiempo(cp)
        salida = parsearDatos(datos)
    return salida


def get(fila):
    cpro = fila['CPRO']
    cmun = fila['CMUN']
    print(f'{2:02d}')
    return f"{int(cpro):02d}{int(cmun):03d}"

def buscar(nombre):
    resultado = df[df["NOMBRE"].str.lower() == nombre.lower()]
    return resultado

def listar(nombre):
    resultado = df[df["NOMBRE"].str.contains(nombre, case=False, na=False)]
    return resultado

def recogerTiempo(municipio):
    url = BASE + endpoint + str(municipio)
    response = requests.get(url, headers=authString)

    print(response.status_code)

    if(response.status_code == 200):
        try:
            jsRespuesta = response.json()
            urlToCall = jsRespuesta['datos']
            prediccion = requests.get(urlToCall, headers=authString)
            # jsData = prediccion.json()
            # Para imprimir el json bonito:
            # print(json.dumps(jsData, indent=4, ensure_ascii=False))
            return prediccion
        except:
            print("Formato de la respuesta erroneo")
            print(response.text)

def parsearDatos(valores):
    print(valores)
    jsData = valores.json()
    valores = jsData[0]

    #Recoger valor
    nombre = valores["nombre"]
    #Recoger valor
    provincia = valores["provincia"]
    prediccion = valores["prediccion"]
    dia = prediccion["dia"]

    #Dia a tratar
    hoy = dia[0]
    #Recoger valor
    cielo = getPeriodo(hoy["estadoCielo"])["descripcion"]
    temperaturas = hoy["temperatura"]
    dato = temperaturas["dato"]
    #Recoger valor
    temperatura = ''
    for p in dato:
        if(p["hora"] == '6'):
            temperatura = p["value"]
            break
    #Recoger valor
    precipitacion = getPeriodo(hoy["probPrecipitacion"])["value"]
    viento = getPeriodo(hoy["viento"])
    #Recoger valor
    dirViento = viento["direccion"]
    #Recoger valor
    vViento = viento["velocidad"]

    salida = {}
    salida["nombre"] = nombre
    salida["provincia"] = provincia
    salida["estadoCielo"] = cielo
    salida["temperatura"] = temperatura
    salida["precipitacion"] = precipitacion
    salida["DireccionViento"] = dirViento
    salida["ValocidadViento"] = vViento
    return salida

def getPeriodo(datos):
    for p in datos:
        if(p['periodo'] == '00-06'):
            return p

def main():
    salida = preguntar('sdajkhask')
    print(json.dumps(salida, indent=4, ensure_ascii=False))
    salida = preguntar('mad')
    print(json.dumps(salida, indent=4, ensure_ascii=False))
    salida = preguntar('madrid')
    print(json.dumps(salida, indent=4, ensure_ascii=False))
    # print(recogerTiempo(28051))

@app.get('/municipio')
def getMunicipioInfo(nombre : str = ''):
    return preguntar(nombre)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port= 8090)
