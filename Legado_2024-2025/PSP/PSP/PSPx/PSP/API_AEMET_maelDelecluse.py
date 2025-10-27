from fastapi import FastAPI, HTTPException
import pandas as pd
import requests
import logging
import uvicorn
from datetime import datetime
import os

# Configuración de rutas y archivos
directorio_base = os.path.dirname(os.path.abspath(__file__))
ruta_archivo_excel = os.path.join(directorio_base, "20codmun.xlsx")

# Cargar datos de municipios
df_municipios = pd.read_excel(ruta_archivo_excel, dtype={"CPRO": str, "CMUN": str, "NOMBRE": str, "PROVINCIA": str})

# Configuración de logging
logging.basicConfig(
    filename=os.path.join(directorio_base, "registro_api.log"),
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

app = FastAPI()
AEMET_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtYWVsZGVsZWNsdXNlQGdtYWlsLmNvbSIsImp0aSI6IjI4YmNkODljLTM5ZDQtNDQ2ZS04NTVjLTNhZTQyZDM0NDI4NyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzQwMjUwMjQyLCJ1c2VySWQiOiIyOGJjZDg5Yy0zOWQ0LTQ0NmUtODU1Yy0zYWU0MmQzNDQyODciLCJyb2xlIjoiIn0.Rgwp7QuBsGY_wSFnNYAJTHfanZX63XdZViZLV8ZYeys"
AEMET_API_URL = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/horaria/"

def obtener_codigo_y_provincia(nombre_municipio: str):
    municipio = df_municipios[df_municipios["NOMBRE"].str.lower() == nombre_municipio.lower()]
    if municipio.empty:
        return None, None
    codigo_municipio = municipio.iloc[0]['CPRO'] + municipio.iloc[0]['CMUN']
    provincia = municipio.iloc[0]['PROVINCIA']
    return codigo_municipio, provincia

def solicitar_prediccion(codigo_municipio: str):
    url = f"{AEMET_API_URL}{codigo_municipio}/?api_key={AEMET_API_KEY}"
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        return None
    datos_json = respuesta.json()
    if "datos" in datos_json:
        url_prediccion = datos_json["datos"]
        respuesta_prediccion = requests.get(url_prediccion)
        if respuesta_prediccion.status_code == 200:
            return respuesta_prediccion.json()
    return None

@app.get("/clima/{municipio}")
def obtener_clima(municipio: str):
    logging.info(f"Consulta de API - Municipio: {municipio}")
    codigo, provincia = obtener_codigo_y_provincia(municipio)
    if not codigo:
        raise HTTPException(status_code=404, detail="Municipio no encontrado")
    
    prediccion = solicitar_prediccion(codigo)
    if not prediccion:
        raise HTTPException(status_code=500, detail="No se pudo obtener la predicción")
    
    respuesta = {
        "municipio": municipio,
        "provincia": provincia,
        "pronostico": []
    }
    
    try:
        pronostico_horas = prediccion[0]['prediccion']['dia'][0]['hora'][:6]
        for hora in pronostico_horas:
            respuesta["pronostico"].append({
                "hora": f"{hora['@periodo']}:00",
                "estado_cielo": hora.get("estadoCielo", {}).get("descripcion", "Desconocido"),
                "temperatura": hora.get("temperatura", "N/A"),
                "precipitacion": hora.get("precipitacion", {}).get("value", "0"),
                "viento_direccion": hora.get("viento", {}).get("direccion", "N/A"),
                "viento_velocidad": hora.get("viento", {}).get("velocidad", "N/A")
            })
    except Exception as error:
        logging.error(f"Error al procesar los datos: {str(error)}")
        raise HTTPException(status_code=500, detail="Error procesando la predicción")
    
    return respuesta

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

