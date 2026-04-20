import requests
from bs4 import BeautifulSoup

# my user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 

# 1. Definimos la URL (usaremos una de prueba o Wikipedia)
url = "https://es.wikipedia.org/wiki/Python_(lenguaje_de_programación)"

#crear diccionario credencial para user agent
cabeceras={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

# 2. Hacemos la petición a la web
respuesta = requests.get(url, headers=cabeceras)

# 3. Convertimos el HTML en un "objeto sopa" fácil de leer
sopa = BeautifulSoup(respuesta.text, 'html.parser')

# 4. Buscamos el título principal (etiqueta <h1>)
titulo = sopa.find('h1').text

print(f"El título de la página es: {titulo}")