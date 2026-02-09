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

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import requests
import json

BASE = 'https://opendata.aemet.es/opendata'
endpoint = '/api/prediccion/especifica/municipio/diaria/'
municipio = '28050'

key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtYXRlb2F5YXJyYWJhcmJlcm9AZ21haWwuY29tIiwianRpIjoiZGE5MmRiZmEtMGFlNy00MzNiLTg0NDAtMDc2MmIyYTYwNDkwIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3NzAwMzU3MTEsInVzZXJJZCI6ImRhOTJkYmZhLTBhZTctNDMzYi04NDQwLTA3NjJiMmE2MDQ5MCIsInJvbGUiOiIifQ.A4szG1CuWFevrxM1SnR_cHLkvJ5-tdPqdD8eqcQWUaQ'

authString = {"api_key": key}

url = BASE + endpoint + municipio

response = requests.get(url, headers=authString)
print(response.status_code)

if(response.status_code == 200):
    try:
        jsRespuesta = response.json()
        print(response.text)
        urlToCall = jsRespuesta['datos']
        prediccion = requests.get(urlToCall, headers=authString)
        jsData = prediccion.json()
        print(json.dumps(jsData, indent=4, ensure_ascii=False))
    except:
        print("Formato de la respuesta erroneo")
        print(response.text)
