import requests
import pandas as pd
from fastapi import FastAPI, HTTPException
import uvicorn

# Creamos la aplicación FastAPI
app = FastAPI()

# Definimos los personajes conocidos y sus códigos correspondientes en la API externa
personajes_conocidos = {
    'Luke': '1',
    'Darth': '4',
    'Leia': '5',
    'Anakin': '11',
    'Chewbacca': '13',
    'Han': '14'
}

# Función para obtener la información de un personaje desde la API externa
def obtener_informacion_personaje(personaje_id):
    url = f"https://swapi.dev/api/people/{personaje_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Función para obtener la información del planeta desde la API externa
def obtener_informacion_planeta(planeta_url):
    response = requests.get(planeta_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Ruta para obtener información de un personaje
# Ahora utilizamos un parámetro en la ruta directamente: "/personaje/{nombre}"
@app.get("/personaje/{nombre}")
async def obtener_personaje(nombre: str):
    # Verificar si el personaje está en la lista de personajes conocidos
    if nombre not in personajes_conocidos:
        raise HTTPException(status_code=404, detail="Personaje no conocido")

    # Obtener el código del personaje
    personaje_id = personajes_conocidos[nombre]
    
    # Obtener la información del personaje desde la API externa
    datos_personaje = obtener_informacion_personaje(personaje_id)
    
    if datos_personaje:
        # Extraemos la información relevante
        color_pelo = datos_personaje['hair_color']
        color_ojos = datos_personaje['eye_color']
        planeta_url = datos_personaje['homeworld']

        # Obtener la información del planeta
        datos_planeta = obtener_informacion_planeta(planeta_url)
        
        if datos_planeta:
            planeta = datos_planeta['name']
        else:
            planeta = "Desconocido"

        # Crear un DataFrame de Pandas con la información
        df = pd.DataFrame([{
            'nombre': datos_personaje['name'],
            'color_pelo': color_pelo,
            'color_ojos': color_ojos,
            'planeta': planeta
        }])

        # Convertimos el DataFrame a diccionario y lo retornamos como JSON
        return df.to_dict(orient="records")[0]

    raise HTTPException(status_code=500, detail="No se pudo obtener la información del personaje")

# Iniciar el servidor con Uvicorn (FastAPI usa Uvicorn como servidor ASGI)
# Ejecutar el servidor con el siguiente comando:
# uvicorn app:app --reload
if _name_ == "_main_":
    uvicorn.run(app, host="localhost", port=8000)