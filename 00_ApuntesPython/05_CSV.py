import os
import pandas as pd

#Recoje la direccion del propio programa
base = os.path.dirname(__file__)
#Le añade la direccion buscada
ruta = os.path.join(base, "ejemplo.csv")

df = pd.read_csv(ruta)

tituloColumnas = df.columns

columna = df["CMUN"]
columna = df.iloc[123:123]
fila = df.loc[123:123]
nombreColumna = tituloColumnas[2]

# Añadir una nueva fila
nueva_fila = {
    "Atr1" : "Valor1",
    "Atr2" : "Valor2",
    "Atr3" : "Valor3"
}

df.loc[len(df)] = nueva_fila

df.to_csv("fichero.csv", index=False)

df = pd.read_csv("fichero.csv")

df.loc[df["NombreAtr/TituloFila"] == "Nombre a buscar", "NombreAtr/TituloFila a actualizar"] = 'Nuevo Valor'

#Comprobar que existe
fila = df[df["NombreAtr/TituloFila"] == "Nombre a buscar"]

if not fila.empty:
    df.loc[fila.index, "NombreAtr/TituloFila a actualizar"] = "Nuevo Valor"

df.to_csv("equipos.csv", index=False)