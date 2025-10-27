import requests
from fastapi import FastAPI
import uvicorn

app = FastAPI()
URL_BASE = "https://swapi.dev/api"

def obtenerInfoPersonaje(personaje_id):
    respuesta = requests.get(f"{URL_BASE}/people/{personaje_id}")
    
    print(respuesta)
    
    if respuesta.status_code != 200:
        return None
    else:
        return respuesta.json()

personajes_por_id = {
    "Luke": 1,
    "C3-PO" : 2
}

def obtenerPlaneta(urlPlaneta):
    infoPlanet = requests.get(urlPlaneta)
    if infoPlanet.status_code != 200:
        return None
    else: return infoPlanet.json()
    
@app.get("/personaje/{nombre}")
def mostrarInfoPersonaje(nombre):
    nombrePersonaje = personajes_por_id[nombre]
    infoPersonaje = obtenerInfoPersonaje(nombrePersonaje)
    
    if not infoPersonaje:
        return "No existe un personaje con ese codigo"

    urlPlanet = infoPersonaje["homeworld"]
    infoPlaneta = obtenerPlaneta(urlPlanet)
    
    return{
        "nombre": infoPersonaje["name"],
        "genero" : infoPersonaje["gender"],
        "fechaNac" : infoPersonaje["birth_year"],
        "planeta" : infoPlaneta["name"]
    }
    
uvicorn.run(app, host= "localhost", port= 8090 )