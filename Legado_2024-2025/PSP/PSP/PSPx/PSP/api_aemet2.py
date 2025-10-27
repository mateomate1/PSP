import requests
import pandas as pd
import os
import logging
import datetime as dt
from fastapi import FastAPI

# Inicializa FastAPI
app = FastAPI()
LOGGER = logging.getLogger(__name__)

def get_prediccion(municipio):
    # Obtiene el directorio actual
    directorio_actual = os.path.dirname(os.path.realpath(__file__))
    fichero_xlsx = os.path.join(directorio_actual, "20codmun.xlsx")
    
    # Carga el archivo Excel con códigos de municipios
    datosFichero = pd.read_excel(fichero_xlsx, dtype={"CPRO": str, "CMUN": str})
    infomunip = datosFichero[datosFichero['NOMBRE'] == municipio]
    
    # Obtiene el código del municipio concatenando CPRO y CMUN
    codigo_munip = str(infomunip.iloc[0,1]) + str(infomunip.iloc[0,2])
    
    # Define la URL base de la API de AEMET
    URLBase = 'https://opendata.aemet.es/opendata'
    endpoint = '/api/prediccion/especifica/municipio/horaria/'
    
    # Clave de acceso a la API (sustituir por una clave válida)
    key = "TU_API_KEY"
    authString = {"api_key": key}
    
    # Construcción de la URL de consulta
    url = URLBase + endpoint + codigo_munip
    
    # Realiza la petición GET a la API
    response = requests.get(url, params=authString)
    if response.status_code == 200:
        try:
            # Obtiene la URL con los datos de la predicción
            jsData = response.json()
            urlDatos = jsData['datos']
            
            # Descarga los datos de la predicción
            prediccion = requests.get(urlDatos)
            return prediccion.json()
        except:
            print("Respuesta no es JSON")
            print(response.text)
    return None

def generar_prediccion_horas(archivo_json):
    try:
        # Extrae datos del JSON obtenido
        municipio = archivo_json[0]["nombre"]
        provincia = archivo_json[0]["provincia"]
        pronostico = []
        dia = archivo_json[0]["prediccion"]["dia"][0]  # Obtiene el primer día de predicción
        
        for i in range(2):  # Obtiene la predicción para las próximas 2 horas
            if i < len(dia["estadoCielo"]):
                hora = dia["estadoCielo"][i].get("periodo")
                estado_cielo = dia["estadoCielo"][i].get("descripcion")
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
        LOGGER.error("Error al procesar el JSON")
        return {}

# Define el endpoint para obtener la predicción
@app.get("/pronostico/{municipio}")
def getLocalidad(municipio: str):
    LOGGER.info(f"Llamada a [/pronostico/{municipio}] a las {dt.datetime.now()}")
    prediccion = get_prediccion(municipio)
    return generar_prediccion_horas(prediccion)

if __name__ == "__main__":
    # Configuración del logging y ejecución del servidor
    logging.basicConfig(filename="predicciones.log", level=logging.INFO)
    uvicorn.run(app, host="localhost", port=1224)