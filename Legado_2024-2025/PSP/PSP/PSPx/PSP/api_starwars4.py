import requests
from fastapi import FastAPI
import uvicorn

app = FastAPI()

def infoPersonaje(personaje_id):
    url = f"https://swapi.dev/api/people/{personaje_id}/"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def infoPlaneta(planeta_url):
    response = requests.get(planeta_url)
    if response.status_code != 200:
        return None
    return response.json()

personajes_conocidos = {
    'Luke': '1',
    'Darth': '4',
    'Leia': '5',
    'Anakin': '11',
    'Chewbacca': '13',
    'Han': '14'
}

@app.get("/personaje/{nombre}")
def mostrarDatosPersonaje(nombre: str):
    personaje_id = personajes_conocidos.get(nombre)
    if not personaje_id:
        return {"error": "Personaje no encontrado"}

    datos = infoPersonaje(personaje_id)
    if not datos:
        return {"error": "No se encontró información del personaje"}
    
    print(datos['name'])
    print(datos['height'])
    print(datos['hair_color'])
    print(datos['eye_color'])

    cod_planeta = datos['homeworld']
    datoplaneta = infoPlaneta(cod_planeta)

    
    return {
        "name": datos['name'],
        "height": datos['height'],
        "hair_color": datos['hair_color'],
        "eye_color": datos['eye_color'],
        "homeworld": datoplaneta['name'] 
        if datoplaneta 
        else "Desconocido"
    }

if _name_ == "_main_":
    uvicorn.run(app, host="localhost", port=8000)