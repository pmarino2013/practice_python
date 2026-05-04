## 🎨 Clase 8: Visualización Creativa (Matplotlib & Seaborn)

**Concepto clave:** El arte de comunicar con datos (_Data Storytelling_).

---

### 1. El Kit Estético (15 min)

Además de `Matplotlib`, introducimos **Seaborn**. Es una librería construida sobre Matplotlib que hace que los gráficos se vean modernos y profesionales con mucho menos código.

**Instalación:**

```powershell
python -m pip install seaborn
```

---

### 2. Tipos de Gráficos para Decisiones de Negocio (35 min)

No se trata de hacer gráficos "lindos", sino de elegir el correcto para cada pregunta:

- **Barras:** Para comparar (¿Quién vendió más?).
- **Líneas:** Para tendencias (¿Las ventas suben o bajan por mes?).
- **Histogramas:** Para distribución (¿Qué rango de precios es el más común?).
- **Scatter Plot (Dispersión):** Para encontrar relaciones (¿Los cursos más caros se venden menos?).

---

### 3. Proyecto Práctico: "Dashboard de Rendimiento Académico" (60 min)

Vamos a usar el archivo `ventas.csv` para crear una figura con múltiples gráficos que resuma todo el trimestre.

**Código que desarrollarán los alumnos:**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Preparación de datos (Repaso Clase 6)
df = pd.read_csv('ventas.csv').dropna()
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%m-%d-%y')
df['Mes'] = df['Fecha'].dt.month_name()

# 2. Configuración estética de Seaborn
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# --- GRÁFICO 1: Ventas por Vendedor (Barras) ---
plt.subplot(1, 2, 1) # 1 fila, 2 columnas, posición 1
sns.barplot(data=df, x='Vendedor', y='Monto', estimator=sum, palette='viridis')
plt.title('Ingresos Totales por Vendedor')
plt.ylabel('Dólares ($)')

# --- GRÁFICO 2: Evolución Temporal (Líneas) ---
plt.subplot(1, 2, 2) # 1 fila, 2 columnas, posición 2
sns.lineplot(data=df.sort_values('Fecha'), x='Fecha', y='Monto', marker='o', color='red')
plt.xticks(rotation=45)
plt.title('Evolución de Ventas en el Tiempo')

# 3. Ajuste final y visualización
plt.tight_layout()
plt.show()
```

---

### 4. Cierre del Módulo 2 (10 min)

Este es el momento de hacer el balance. Los alumnos han pasado de no saber qué es un `.csv` a:

1.  Extraer datos de la web automáticamente.
2.  Limpiar errores y manejar fechas.
3.  Generar reportes visuales listos para una reunión de directorio.

**Gancho para el Módulo 3:**
"Hasta ahora, nosotros le decimos a Python qué buscar. A partir de la próxima clase, en el **Módulo 3: Inteligencia Artificial**, vamos a enseñarle a la computadora a 'ver' por sí misma usando **OpenCV**. Pasaremos de analizar tablas a analizar píxeles en tiempo real".

---

### 🛠️ Reto Final del Módulo:

Crea un gráfico de "Torta" (Pie Chart) que muestre qué porcentaje de las ventas totales representa cada **Producto**. Personaliza los colores para que coincidan con la marca de la academia.
