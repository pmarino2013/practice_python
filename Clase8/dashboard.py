import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Preparación de datos (Repaso Clase 6)
df = pd.read_csv('../archivo/ventas.csv').dropna()
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%m-%d-%y')
df['Mes'] = df['Fecha'].dt.month_name() #creamos serie Mes y cargamos los meses de cada fila

# 2. Configuración estética de Seaborn
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6)) # tamaño del gráfico (ancho, alto) en pulgadas

# --- GRÁFICO 1: Ventas por Vendedor (Barras) ---
plt.subplot(1, 2, 1) # 1 fila, 2 columnas, posición 1
sns.barplot(data=df, x='Vendedor', y='Monto', estimator=sum, palette='viridis')
plt.title('Ingresos Totales por Vendedor')
plt.ylabel('Dólares ($)')

# --- GRÁFICO 2: Evolución Temporal (Líneas) ---
plt.subplot(1, 2, 2) # 1 fila, 2 columnas, posición 2
sns.lineplot(data=df.sort_values('Fecha'), x='Fecha', y='Monto', marker='o', color='red')
plt.xticks(rotation=45) # rotar etiquetas del eje x para mejor legibilidad
plt.title('Evolución de Ventas en el Tiempo')

# 3. Ajuste final y visualización
plt.tight_layout() # ajusta automáticamente el espacio entre subplots para evitar solapamientos
plt.show() # muestra el dashboard con ambos gráficos