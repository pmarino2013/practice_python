import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_PIB_(nominal)"
headers = {"User-Agent": "Mozilla/5.0"}

respuesta = requests.get(url, headers=headers)
sopa = BeautifulSoup(respuesta.text, "html.parser")

pib=[]


datos=sopa.find('tbody', id='mwNg')
filas=datos.find_all('tr')

for fila in filas:
    datitos = []  # Resetear la lista para cada fila
    celdas = fila.find_all('td')  # Buscar celdas EN ESTA FILA
    
    for celda in celdas:
        unit = celda.find_all('span')
        valor = ""
        if len(unit) > 0:
            if len(unit)<3:
                valor = unit[1].text
            else:
                valor = unit[0].text
        else:
            valor = celda.text
        
        datitos.append(valor)
    
    # Crear diccionario si hay datos
    if len(datitos) >= 3:
        prov = {
            "pos": datitos[0],
            "pais": datitos[1],
            "pib": int(re.sub(r'\D', '', datitos[2]))  # Elimina todo lo que no sea dígito
        }
        if prov["pos"]!="":
            pib.append(prov)
     


df = pd.DataFrame(pib)

# print(df.info())
promedio_pib = df['pib'].mean()
menor_pib = df[df['pib'] <2000]


print("--- PIB MUNDIAL ---")
print(f"Promedio: {promedio_pib:.2f}")
print(f"Lista de los paises con PIB menor a los 2mil")
print(menor_pib[['pais','pib']])

