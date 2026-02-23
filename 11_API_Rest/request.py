import requests
from requests.auth import HTTPBasicAuth
import json

ip = 'http://localhost'
port = '8090'
URL_base = f'http://{ip}:{port}'

def procesar(response):
    if response.status_code == 200:
        try:
            jsData = response.json()
            imprimirJsonBonito(jsData)
        except:
            print("Error en la respuesta")
            print(response.text)
    else:
        print(response.text)
        print(response.reason)

def imprimirJsonBonito(jsData):
    print(json.dumps(jsData, indent=4, ensure_ascii=False))

def main():
    while True:
        entrada = input('Introduzca un municipio(0 para salir): ')
        if entrada==0:
            break
        else:
            response = requests.get(f'{URL_base}/municipio?{entrada}')
            jsData = procesar(response)
            imprimirJsonBonito()

if __name__ == '__main__':
    main()