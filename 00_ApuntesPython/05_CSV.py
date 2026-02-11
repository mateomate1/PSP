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
