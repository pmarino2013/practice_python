# Módulo 1: Automatización y Lógica

_El arte de delegar tareas repetitivas a la computadora._

## 1. El Despegue: Entorno y Primeras Instrucciones

Para comenzar, Python utiliza una sintaxis clara y legible. La función `print()` es nuestra ventana de salida, mientras que `input()` nos permite recibir información del usuario.

### Conceptos Clave:

- **Variables:** Espacios de memoria con un nombre descriptivo.
- **Comentarios:** Usamos `#` para explicar el código (no se ejecutan).

### Ejemplo de "Echo-Bot":

```python
# Definición de una variable mediante entrada del usuario
usuario = input("¿Cómo te llamas? ")

# Salida de datos usando f-strings (formatos de cadena)
print(f"Hola {usuario}, bienvenido al curso de Python.")
```

---

## 2. Datos y Decisiones (Estructuras Condicionales)

Python clasifica la información en tipos: `int` (enteros), `float` (decimales), `str` (texto) y `bool` (booleano: True/False). La lógica de programación se basa en la toma de decisiones mediante `if`, `elif` y `else`.

### Operadores lógicos:

- `==` (Igualdad)
- `!=` (Diferente)
- `>` / `<` (Mayor o menor que)

### Ejemplo de Validador de Acceso:

```python
password_db = "Python123"
intento = input("Introduce la contraseña: ")

if intento == password_db:
    print("Acceso concedido.")
elif intento == "1234":
    print("Esa contraseña es demasiado simple. Intenta de nuevo.")
else:
    print("Contraseña incorrecta.")
```

---

## 3. El Poder de la Repetición (Listas y Bucles)

Las **listas** son colecciones ordenadas de elementos. Para recorrerlas o repetir acciones, utilizamos bucles:

- **`for`**: Ideal cuando sabemos cuántas veces repetir (por ejemplo, para cada elemento de una lista).
- **`while`**: Se ejecuta mientras una condición sea verdadera.

### Ejemplo de Gestor de Inventario:

```python
frutas = ["Manzana", "Banana", "Cereza"]

# Agregar un elemento
frutas.append("Naranja")

# Recorrer la lista con un bucle for
print("Lista de productos:")
for fruta in frutas:
    print(f"- {fruta}")
```

---

## 4. Código Profesional: Funciones y Persistencia

Para evitar repetir código, lo agrupamos en **funciones** usando la palabra reservada `def`. Además, la persistencia permite que los datos no se borren al cerrar el programa mediante el manejo de archivos.

### Ejemplo de Bitácora con Guardado:

```python
import datetime

def guardar_nota(texto):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    # El modo 'a' (append) agrega contenido sin borrar el anterior
    with open("bitacora.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] - {texto}\n")
    print("Nota guardada exitosamente.")

# Uso de la función
mi_nota = input("Escribe un pensamiento para tu bitácora: ")
guardar_nota(mi_nota)
```

###
