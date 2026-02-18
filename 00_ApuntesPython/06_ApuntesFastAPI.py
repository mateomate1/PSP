#Creacion API con FastAPI
from fastapi import FastAPI, Security, HTTPException, status, Depends, Body
from fastapi.security import APIKeyHeader
import uvicorn
from pydantic import BaseModel
#Request a una api
import requests
from requests.auth import HTTPBasicAuth
#Trata de datos de json
import json

#En caso de querer encenderla sin control de acceso
app = FastAPI()

#En caso de querer usar control de acceso
api_key = APIKeyHeader(name="api_key")
def check(api_key_header: str = Security(api_key)):
    if api_key_header == "Clave":
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Mensaje para el cliente",
            headers={"WWW-Authenticate": "Basic"},
        )
app = FastAPI(dependencies=[Depends(check)])

#ENDPOINTS ------->

#http://.../x siendo x una variable
@app.get("/{x}")
def leer_x(x: str):
    return f'Buenos dias {x}'

#Se puede extender lo que se considere necesario:
@app.get('/{x}/{y}')
def leer_variovalor(x: str, y: int):
    return f'Me llamo {x} y tengo {y} años'

#http://.../municipio?cp=28050
#El metodo recibe cp, como string y por valor le asigna 28050
@app.get('/municipio')
def obtener_nombre_municipio(cp:str = 28050):
    return{"municipio" :"procesarInfo"}

#Si no se le asigna un valor por defecto el valor pasa a ser obligatorio
@app.get('/municipio')
def obtener_nombre_municipio_cp_obligatorio(cp:str):
    return {"municipio": "procesarInfo"}

#En caso de querer varios valores asi:
@app.get('/persona')
def definirPersona(nombre:str, edad:str):
    return f'Has creado a {nombre}, con {edad} años'
#Se le llama asi:
#http://.../persona?nombre=mateo&edad=22

#En caso de querer varios valores pasados por json en el body de la request hay 3 metodos:
#1 Pedirle que pase un dict
@app.post('/addjson')
def update(datos:dict = Body()):
    return f'Buenos dias {datos.get('nombre')}, el dia {datos.get('fNac')}, cumples anos, felicidades'

#2 Recuperar los datos directamente del body
@app.post('addjson')
def update(
    nombre:str = Body(),
    edad:int = Body(),
    curso:str = Body()
):
    return f'{nombre} tiene {edad} anos y esta en el curso {curso}'

#3 Crear una clase y que se mapee con BaseModel de pydantic
class Usuario(BaseModel):
    nombre: str
    edad: int
    activo: bool

#En este caso usuario_id lo recibe como atributo html
@app.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: Usuario):
    return {
        "id": usuario_id,
        "nombre": usuario.nombre,
        "edad": usuario.edad,
        "activo": usuario.activo
    }

#Procesar respuestas:

def procesa(response):
    print(response.status_code)
    # Procesamos respuesta
    if response.status_code == 200:
        #print(response.content)
        # CUIDADO: Si la respuesta no es JSON dará error. Se recomienda incluir en un try
        try:
            jsData = response.json()
            print(jsData)
            imprimirJsonBonito(jsData)
        except:
            print("Respuesta no es JSON")
            print(response.text)
    else:
        print(response.text)
        print(response.reason)

def imprimirJsonBonito(jsData):
    print(json.dumps(jsData, indent=4, ensure_ascii=False))

def hacer_peticion(endpoint, param1, param2):
    URLBase = 'http://192.168.1.23:8090'

    #Llamada sin parametros especiales:
    response = requests.get(URLBase + endpoint)

    #Llamada con parametros(URLBASE/ENDPOINT?param=value&paramX=valueX...)
    parametros = {
        "paramName" : "value"
        , "paramX" : "valueX"
        }
    response = requests.get(URLBase + endpoint, params=parametros)
    #Esto es lo mismo que
    response = requests.get(URLBase + endpoint, params={"paramName" : "value", "paramX" : "valueX"})

    #Llamada con parametros en la url:
    response.requests.get(URLBase+endpoint+f'/{param1}/{param2}/...')

    #Procesar Respuesta:
    procesa(response)

#Inicializar API
if __name__ == "__main__":
    #La ip tiene que ser exacta, no vale con poner localhost o 192.168.1....
    #Localhost solo seria valido para uno mismo, sin embargo no cambia
    IP = 'localhost'
    #La ip especifica seria correcta en caso de que sea para otros la api,
    #sin embargo cambia con el host de la conexion
    IP = '192.168.1.26'
    uvicorn.run(app, host="IP", port=8090)
    #Al correrlo con uvicorn se genera una documentacion automatica en URL_base/docs
    #Ejemplo: http://localhost:8090/docs