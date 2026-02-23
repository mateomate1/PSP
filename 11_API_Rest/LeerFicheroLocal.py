import os
import pandas as pd

base = os.path.dirname(__file__)
ruta = os.path.join(base, "20codmun.csv")

df = pd.read_csv(ruta)

def buscar(nombre):
    resultado = df[df["NOMBRE"].str.lower() == nombre.lower()]
    return resultado

def listar(nombre):
    resultado = df[df["NOMBRE"].str.contains("mad", case=False, na=False)]["NOMBRE"].tolist()
    return resultado

print(listar('bo'))