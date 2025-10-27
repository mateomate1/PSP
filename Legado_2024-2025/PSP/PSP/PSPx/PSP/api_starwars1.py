import requests
from fastapi import FastAPI
import uvicorn
import json

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

def obtenerPeliculas(urlPeliculas):
    listaPelis = []
    for i in urlPeliculas:
        infopeli = requests.get(i)
        if infopeli.status_code != 200:
            return None
        else: listaPelis.append(infopeli.json())  
    return listaPelis
    
@app.get("/personaje/{nombre}")
def mostrarInfoPersonaje(nombre):
    nombrePersonaje = personajes_por_id[nombre]
    infoPersonaje = obtenerInfoPersonaje(nombrePersonaje)
    
    if not infoPersonaje:
        return "No existe un personaje con ese codigo"

    urlPeli = infoPersonaje["films"]
    infopelis = obtenerPeliculas(urlPeli) #info pelis son varias peliculas por lo que tengo que recorrerlo al printearlo
    
    titulosPeliculas = []
    for p in infopelis:
        titulosPeliculas.append(p["title"])
    
    return{
        "nombre": infoPersonaje["name"],
        "genero" : infoPersonaje["gender"],
        "fechaNac" : infoPersonaje["birth_year"],
        "peliculas" : titulosPeliculas
    }
    
uvicorn.run(app, host= "localhost", port= 8090 )