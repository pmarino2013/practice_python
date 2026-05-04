### 1. Importar las librerías

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

- `pandas` se usa para leer y manejar datos en tablas.
- `matplotlib.pyplot` permite crear gráficos.
- `seaborn` hace que los gráficos se vean más bonitos y simples.

---

### 2. Leer y preparar los datos

```python
df = pd.read_csv('ventas.csv').dropna()
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%m-%d-%y')
df['Mes'] = df['Fecha'].dt.month_name()
```

- `pd.read_csv('ventas.csv')` abre el archivo `ventas.csv` y lo convierte en una tabla.
- `.dropna()` quita filas que tienen valores vacíos.
- `pd.to_datetime(...)` transforma la columna `Fecha` de texto a fecha real de Python.
- Después creamos una nueva columna `Mes` con el nombre del mes de cada fecha.

---

### 3. Configurar el estilo del gráfico

```python
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))
```

- `sns.set_theme(style="whitegrid")` aplica un estilo con fondo claro y líneas de cuadrícula.
- `plt.figure(figsize=(12, 6))` define el tamaño de la imagen completa donde estarán los gráficos.

---

### 4. Primer gráfico: barras de ventas por vendedor

```python
plt.subplot(1, 2, 1)
sns.barplot(data=df, x='Vendedor', y='Monto', estimator=sum, palette='viridis')
plt.title('Ingresos Totales por Vendedor')
plt.ylabel('Dólares ($)')
```

- `plt.subplot(1, 2, 1)` divide la figura en 1 fila y 2 columnas; este es el primer espacio.
- `sns.barplot(...)` crea un gráfico de barras.
- `x='Vendedor'` usa la columna `Vendedor` para el eje horizontal.
- `y='Monto'` usa la columna `Monto` para el eje vertical.
- `estimator=sum` suma los montos de cada vendedor para mostrar el total.
- `palette='viridis'` elige una paleta de colores para el gráfico.
- `plt.title(...)` y `plt.ylabel(...)` ponen título y etiqueta al eje vertical.

---

### 5. Segundo gráfico: evolución de ventas en el tiempo

```python
plt.subplot(1, 2, 2)
sns.lineplot(data=df.sort_values('Fecha'), x='Fecha', y='Monto', marker='o', color='red')
plt.xticks(rotation=45)
plt.title('Evolución de Ventas en el Tiempo')
```

- `plt.subplot(1, 2, 2)` usa el segundo espacio de la misma figura.
- `df.sort_values('Fecha')` ordena los datos por fecha antes de graficar.
- `sns.lineplot(...)` dibuja una línea que muestra cómo cambian las ventas con el tiempo.
- `marker='o'` pone puntos en cada dato.
- `color='red'` pinta la línea de rojo.
- `plt.xticks(rotation=45)` gira las etiquetas de fecha para que se lean mejor.
- `plt.title(...)` pone el nombre del gráfico.

---

### 6. Ajustar espacio y mostrar el gráfico

```python
plt.tight_layout()
plt.show()
```

- `plt.tight_layout()` ajusta los elementos para que no se monten entre sí.
- `plt.show()` muestra la ventana con los dos gráficos.

---

## Resumen para compartir

- Lee los datos con `pandas`.
- Limpia datos vacíos y convierte fechas correctamente.
- Crea dos gráficos en una misma ventana:
  1. Barras por vendedor.
  2. Línea de ventas en el tiempo.
- Usa `seaborn` para que el gráfico sea más fácil de ver.
- Finalmente, muestra todo con `plt.show()`.
