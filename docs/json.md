# Manejar caracteres especiales como acentos (ej. é, ñ, á) al usar la librería `json` en Python

### 1. **Al escribir JSON (usando `json.dump` o `json.dumps`)**

- Usa `ensure_ascii=False` para evitar que los caracteres se conviertan en escapes Unicode.
- Especifica `encoding='utf-8'` al abrir el archivo para asegurar que se guarde correctamente.

**Ejemplo de código para escribir un diccionario en JSON con acentos:**

```python
import json

# Datos de ejemplo con acentos
data = [
    {"nombre": "Pablo", "tel": "113456789", "email": "pmarino@gmail.com"},
    {"nombre": "José", "tel": "113423456", "email": "josé@outlook.com"},  # Acento en "José"
    {"nombre": "Silvina", "tel": "112345678", "email": "silvi@gmail.com"},
    {"nombre": "Alberto", "tel": "112345678", "email": "albert@yahoo.com"}
]

# Escribir a archivo JSON con acentos preservados
with open('archivos/agenda.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)  # indent para formato legible
```

- Esto guardará el archivo con los acentos intactos (ej. "José" en lugar de "Jos\u00e9").
- Si usas `json.dumps()` para una cadena, es similar: `json.dumps(data, ensure_ascii=False)`.

### 2. **Al leer JSON (usando `json.load` o `json.loads`)**

- Especifica `encoding='utf-8'` al abrir el archivo.
- `json.load()` automáticamente decodificará los escapes Unicode si existen, pero con UTF-8, los acentos se mantendrán.

**Ejemplo de código para leer el JSON:**

```python
import json

# Leer desde archivo JSON
with open('archivos/agenda.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Imprimir para verificar (los acentos se mostrarán correctamente)
for persona in data:
    print(f"Nombre: {persona['nombre']}, Email: {persona['email']}")
```

- Si el archivo ya tiene escapes Unicode (como en tu selección actual), `json.load()` los convertirá automáticamente a caracteres reales al cargarlos en Python.

### 3. **Si el archivo ya tiene escapes Unicode (como `\u00e9`)**

- Si tu `agenda.json` actual tiene escapes (probablemente porque se guardó sin `ensure_ascii=False`), puedes "repararlo" reescribiéndolo con el código de escritura anterior.
- Una vez cargado con `json.load()`, los datos en Python tendrán los acentos correctos, y al reescribir con `ensure_ascii=False`, se guardarán sin escapes.

### 4. **Consejos adicionales**

- **Codificación del archivo:** Asegúrate de que tu editor (como VS Code) guarde el archivo en UTF-8. En VS Code, ve a "Archivo > Guardar con codificación > UTF-8".
- **Errores comunes:** Si ves errores como `UnicodeDecodeError`, es porque el archivo no está en UTF-8. Convierte el archivo a UTF-8 manualmente o usa herramientas como `chardet` para detectar la codificación.
- **Para strings en memoria:** Si trabajas con JSON en strings (no archivos), usa `json.dumps(data, ensure_ascii=False)` y `json.loads(string)`.
- **Compatibilidad:** Esto funciona en Python 3. Si usas Python 2, considera actualizar, ya que maneja Unicode mejor.
