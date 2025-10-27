import requests
import pandas as pd
import fastapi
import uvicorn

from fastapi import FastAPI

app = fastapi.FastAPI()

IDS = {
    "luke": 1,
    "darth": 4,
    "leia": 5,
    "anakin": 11,
    "chewbacca": 13,
    "han": 14
}

SWAPI_URL = "https://swapi.dev/api/people/"

def get_character_data(id_personaje: int):
    respuesta = requests.get(f"{SWAPI_URL}{id_personaje}/")
    data = respuesta.json()

    planeta_url = data.get("homeworld")
    planeta_nombre = ""
    if planeta_url:
        planeta_respuesta = requests.get(planeta_url)
        if planeta_respuesta.status_code == 200:
            planeta_nombre = planeta_respuesta.json().get("name")

    return {
        "nombre_completo": data.get("name"),
        "color_pelo": data.get("hair_color"),
        "color_ojos": data.get("eye_color"),
        "planeta_origen": planeta_nombre
    }

@app.get("/personaje/")
def get_character(nombre: str):
    id_personaje = IDS.get(nombre)
    if not id_personaje:
        return {"mensaje": "no encontrado"}
    
    character_data = get_character_data(id_personaje)
    if not character_data:
        return {"mensaje": "no encontrado"}
    
    return character_data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
