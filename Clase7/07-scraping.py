import requests
from bs4 import BeautifulSoup
# from bs4 → Indica que estamos importando desde la librería BeautifulSoup4 (bs4 es su nombre corto)
# import BeautifulSoup → Importamos específicamente la clase BeautifulSoup

url="https://es.wikipedia.org/wiki/Inteligencia_artificial"


cabeceras = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

respuesta= requests.get(url,headers=cabeceras)

sopa=BeautifulSoup(respuesta.text,"html.parser")


numeracion=0
titulo=sopa.find('h1').text
subtitulo = sopa.find('h2', id="Historia").text

lista=sopa.find('ul', id='mwAXc')
if lista:
    # 2. Extraemos todos los 'li' que están DENTRO de esa lista
    elementos = lista.find_all('li')
    
    # 3. Guardamos solo el texto en una lista de Python limpia
    datos_finales = []
    for item in elementos:
         datos_finales.append(item.text) 


    print(f"--- {titulo} ---")
    for dato in datos_finales:
        numeracion+=1
        item= f"{numeracion} - {dato}"
    
        with open(f"../archivo/{titulo}_{subtitulo}.txt","a", encoding="utf-8") as f:
            f.write(item+"\n")
    # print(f"Hemos extraído {len(datos_finales)} elementos:")
    # print(datos_finales)
else:
    print("No se encontró ninguna lista con ese ID.")


# print(lista)

# id="mwAXc"