from flask import Flask, request, jsonify
import requests
import logging
import pandas as pd
from datetime import datetime

API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMDAxZ2cwMEBnbWFpbC5jb20iLCJqdGkiOiJiNGU3YzA0Yi1jNmYxLTRiMGItYTNmZS00ZTc5NWU5NmY5Y2IiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTczNzM3NzgzOSwidXNlcklkIjoiYjRlN2MwNGItYzZmMS00YjBiLWEzZmUtNGU3OTVlOTZmOWNiIiwicm9sZSI6IiJ9.peej9wBY3uIDuUfPZufbsU15jmyp5Rc-UMFXo-7GxE8"  
BASE_URL = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/horaria/"
LOG_FILE = "api_calls.log"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='Llamada API: %(asctime)s')

df_municipios = pd.read_csv("20codmun.csv", dtype={'CPRO': str, 'CMUN': str})
df_municipios["CODMUN"] = df_municipios["CPRO"] + df_municipios["CMUN"]

app = Flask(__name__)

@app.route("/pronostico", methods=["GET"])
def get_pronostico():
    municipio = request.args.get("municipio")
    if not municipio:
        return jsonify({"error": "Tienes que poner un municipio"}), 400
    
    municipio_data = df_municipios[df_municipios["NOMBRE"] == municipio]
    if municipio_data.empty:
        return jsonify({"error": "Municipio no encontrado"}), 404
    
    cod_mun = municipio_data.iloc[0]["CODMUN"]
    provincia = municipio_data.iloc[0]["PROVINCIA"]
    
    url = f"{BASE_URL}{cod_mun}/?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Fallo al pedir los datos a AEMET"}), 500
    
    data_url = response.json().get("datos")
    if not data_url:
        return jsonify({"error": "No hay datos disponibles"}), 500
    
    response_data = requests.get(data_url).json()
    pronostico = response_data["prediccion"]["hora"][:6]
    
    resultado = {
        "municipio": municipio,
        "provincia": provincia,
        "pronostico": []
    }
    
    for hora in pronostico:
        resultado["pronostico"].append({
            "hora": hora["fecha"],
            "estado_cielo": hora["estadoCielo"],
            "temperatura": hora["temperatura"],
            "precipitacion": hora["precipitacion"],
            "viento": {
                "direccion": hora["direccionViento"],
                "velocidad": hora["velocidadViento"]
            }
        })
    
    logging.info("Llamada API realizada")
    return jsonify(resultado)

if __name__ == "__main__":
    print("Iniciando servidor Flask...")
    app.run(debug=True)
