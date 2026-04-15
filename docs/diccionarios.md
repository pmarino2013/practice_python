## 📂 Clase 5: Estructuras Maestras (Diccionarios y JSON)

**Concepto clave:** Organización de datos mediante etiquetas (Clave-Valor).

---

### 1. ¿Qué es un Diccionario?

Hasta ahora usábamos **Listas**, donde los datos se guardan por orden (0, 1, 2...). Pero en la vida real, los datos tienen nombres.

- **La analogía:** Una lista es una fila de personas. Un diccionario es una carpeta donde cada dato tiene una etiqueta.
- **Sintaxis:**
  ```python
  # Estructura: { "clave": "valor" }
  usuario = {
      "nombre": "Lucas",
      "edad": 28,
      "es_alumno": True
  }
  ```
- **Acceso:** `print(usuario["nombre"])` (Mucho más legible que `usuario[0]`).

---

### 2. Formato JSON: El lenguaje de Internet

Explicamos que **JSON** (_JavaScript Object Notation_) es el estándar que usan todas las aplicaciones (Instagram, WhatsApp, Bancos) para enviarse datos.

- **Dato vital:** ¡JSON es idéntico a los diccionarios de Python!
- **La librería `json`**: Aprendemos a transformar un diccionario en un archivo real que otras apps puedan leer.

---

### 3. Proyecto Práctico: "La Agenda de Contactos Inteligente"

Vamos a construir un sistema donde cada contacto no es solo un nombre, sino un conjunto de datos (Teléfono, Email, Ciudad).

**El flujo del programa:**

1.  El usuario ingresa los datos de un contacto.
2.  Python los guarda en un diccionario.
3.  Ese diccionario se añade a una lista de "Contactos".
4.  La lista entera se guarda en un archivo llamado `agenda.json`.

**Código base para los alumnos:**

```python
import json
import os
import subprocess

def limpiar():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

# Intentamos cargar datos existentes para no empezar de cero
if os.path.exists("agenda.json"):
    with open("agenda.json", "r") as f:
        contactos = json.load(f)
else:
    contactos = []

while True:
    print("\n--- AGENDA CLOUD 2.0 ---")
    print("1. Agregar | 2. Mostrar Todos | 3. Salir")
    opc = input("Selecciona: ")

    if opc == "1":
        # Creamos el diccionario del contacto
        nuevo = {
            "nombre": input("Nombre: "),
            "tel": input("Teléfono: "),
            "email": input("Email: ")
        }
        contactos.append(nuevo)

        # Guardamos TODO en el archivo JSON
        with open("agenda.json", "w") as f:
            json.dump(contactos, f, indent=4) # indent=4 lo hace legible
        print("✅ Guardado en la nube local.")

    elif opc == "2":
        limpiar()
        print("--- LISTA DE CONTACTOS ---")
        for c in contactos:
            print(f"👤 {c['nombre']} - 📞 {c['tel']} - 📧 {c['email']}")

    elif opc == "3":
        break
```

---

### 4. Cierre y Gancho

- **Logro:** Han aprendido a estructurar datos complejos. Ya no son solo "palabras", son objetos con propiedades.
- **Spoiler Clase 6:** "Cargar 10 contactos es fácil, pero... ¿qué pasa si tenemos un Excel con 1.000.000 de ventas? No podemos usar un `for`. En la próxima clase conoceremos a la bestia: **Pandas**, para procesar montañas de datos en milisegundos".

---

### 🛠️ Reto para el alumno:

Modificar la agenda para que, al mostrar los contactos, si el email termina en `@gmail.com`, le ponga una etiqueta que diga `[CUENTA GOOGLE]`. (Uso de `if` + diccionarios).

---

Para trabajar con la librería `json` en Python, la documentación oficial se centra en **cuatro métodos principales**. La clave para no confundirse es entender si estás trabajando con un **String** (texto en memoria) o con un **Archivo** (físico en el disco duro).

Aquí tienes el desglose técnico:

---

### 1. Los 4 Métodos Fundamentales

Se dividen en dos parejas según su función: **Serializar** (convertir de Python a JSON) y **Deserializar** (convertir de JSON a Python).

#### A. Para manejar Archivos (Sin la "s")

Estos métodos se usan junto con la instrucción `with open()`.

- **`json.dump(objeto, archivo)`**: Toma un diccionario/lista de Python y lo **vuelca** directamente dentro de un archivo `.json`.
- **`json.load(archivo)`**: **Carga** el contenido de un archivo `.json` y lo transforma automáticamente en un objeto de Python (diccionario o lista).

#### B. Para manejar Strings (Con la "s" de _String_)

Se usan cuando el JSON ya es una cadena de texto, por ejemplo, lo que recibes de una API de internet.

- **`json.dumps(objeto)`**: Convierte un objeto Python en un **String** con formato JSON. Útil para imprimirlo o enviarlo por red.
- **`json.loads(string_json)`**: Toma un texto que tiene formato JSON y lo **carga** como un objeto Python.

---

### 2. Ejemplos Prácticos

#### Guardar y Leer un Archivo (`dump` / `load`)

```python
import json

data = {"curso": "Python Pro", "alumnos": 25}

# GUARDAR: Usamos dump
with open("data.json", "w") as f:
    json.dump(data, f, indent=4) # indent=4 lo hace legible para humanos

# LEER: Usamos load
with open("data.json", "r") as f:
    datos_recuperados = json.load(f)
    print(datos_recuperados["curso"])
```

#### Convertir a Texto (`dumps` / `loads`)

```python
import json

# De Diccionario a Texto (Útil para depuración)
usuario = {"id": 1, "nombre": "Ana"}
texto_json = json.dumps(usuario)
print(type(texto_json)) # <class 'str'>

# De Texto a Diccionario
json_recibido = '{"status": "OK", "codigo": 200}'
diccionario = json.loads(json_recibido)
print(diccionario["status"]) # OK
```

---

### 3. Parámetros Importantes de la Documentación

Cuando uses estos métodos, hay tres argumentos que te harán la vida más fácil:

1.  **`indent`**: (Solo en `dump/dumps`) Define cuántos espacios de sangría tendrá el archivo. Sin esto, el JSON se guarda en una sola línea gigante.
2.  **`sort_keys`**: Si lo pones en `True`, ordena las claves del diccionario alfabéticamente.
3.  **`ensure_ascii`**: Si trabajas con caracteres especiales (ñ, tildes), ponlo en `False` para que se guarden correctamente y no como códigos extraños (ej: `\u00f1`).

---

### 💡 Resumen para el curso (Clase 5):

- **Si tiene "s" (`loads`, `dumps`):** Trabaja con **S**trings.
- **Si NO tiene "s" (`load`, `dump`):** Trabaja con archivos (ficheros).
