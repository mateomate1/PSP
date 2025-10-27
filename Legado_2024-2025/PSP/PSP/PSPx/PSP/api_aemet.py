import requests
import json
import pandas as pd
import os
import fastapi
import uvicorn
import logging
import datetime as dt



app = fastapi.FastAPI()
LOGGER = logging.getLogger(__name__)

def get_prediccion(municipio):
    directorio_actual = os.path.dirname(os.path.realpath(__file__))
    fichero_xlsx = directorio_actual+"/20codmun.xlsx"

    datosFichero = pd.read_excel(fichero_xlsx, dtype={"CPRO":str, "CMUN":str})
    infomunip = datosFichero[datosFichero['NOMBRE']==municipio]
    #esto es el municipio
    codigo_munip =str(infomunip.iloc[0,1])+str(infomunip.iloc[0,2])

    print(codigo_munip)

    #esto es la parte de la url que siempre va a estar
    URLBase = 'https://opendata.aemet.es/opendata'
    #y esto es la parte de la url mas especifica 
    endpoint = '/api/prediccion/especifica/municipio/horaria/'

    #esto es la key que necesito para que me acepte la entrada, es como una contraseña
    key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJpbmlnby5kZXNpbHZhY3Vlc3RhQGdtYWlsLmNvbSIsImp0aSI6IjQxZWI1NjRkLTNhY2YtNDU3Zi1iYmRmLThjNGVjY2E1M2E0ZCIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzM3NzE3Mzc4LCJ1c2VySWQiOiI0MWViNTY0ZC0zYWNmLTQ1N2YtYmJkZi04YzRlY2NhNTNhNGQiLCJyb2xlIjoiIn0.l3pjxIZJC0hw3UnBK0lulg788Mn91SS_ih09j5-AUrE"

    #esto es el dict(?) que entra como parametro
    authString = {"api_key": key}

    #aqui junto las partes de la url y la imprimo para saber como estan
    url = URLBase + endpoint + codigo_munip
    print(url)

    #aqui hago la request e imprimo el codigo de respuesta
    response = requests.get(url, params=authString)
    print(response.status_code)

    if response.status_code == 200: #si es exito 
        try:#esto es porque decia que si no es un formato json da excepcion
            #con esto adquiero la url donde estan los datos solicitados
            jsData = response.json()
            urlDatos = jsData['datos']
            #y con esto la informacion dentro de la url
            prediccion = requests.get(urlDatos)
            return prediccion.json()

        except:#si da error
            print("Respuesta no es JSON")
            print(response.text)
    else:#si no es exito
        print(response.text)
        print(response.reason)

def generar_prediccion_horas(archivo_json):

    num_horas = 2
    try:
        municipio = archivo_json[0]["nombre"]
        provincia = archivo_json[0]["provincia"]
        pronostico = []

        dia = archivo_json[0]["prediccion"]["dia"][0]#variable dia donde estan todas las predicciones
        
        for i in range(num_horas):
            if i < len(dia["estadoCielo"]):
                hora = dia["estadoCielo"][i].get("periodo")
                estado_cielo = dia["estadoCielo"][i].get("descripcion")
            else:
                break

            temperatura = dia["temperatura"][i].get("value")
            precipitacion = dia["precipitacion"][i].get("value")                         
            
            pronostico.append({
            "hora": hora,
            "estado_cielo": estado_cielo,
            "temperatura": temperatura,
            "precipitacion": precipitacion,
        })
        
        return {
            "municipio": municipio,
            "provincia": provincia,
            "pronostico": pronostico
        }
    except:
        LOGGER.error("Error al limpiar el json")
    
@app.get("/pronostico/{municipio}")
def getLocalidad(municipio):
   LOGGER.info("Se ha realizado una llamada a [/pronostico/"+municipio+"] a las {}".format(dt.datetime.now()))
   prediccion = get_prediccion(municipio)
   return generar_prediccion_horas(prediccion)

if __name__ == "__main__":
    logging.basicConfig(filename="predicciones.log", level=logging.INFO)

    LOGGER.info("API iniciada en {}".format(dt.datetime.now()))
    uvicorn.run(app, host="localhost", port=1224)
    LOGGER.info("FIN en {}".format(dt.datetime.now()))
   