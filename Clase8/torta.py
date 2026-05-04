import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carga y limpieza de datos
df = pd.read_csv('../archivo/ventas.csv')
df_limpio = df.dropna()  # Eliminamos la fila incompleta de Luis

# 2. Agrupamos por producto y sumamos los montos
# Esto nos da el total de dinero generado por cada item
ventas_por_producto = df_limpio.groupby('Producto')['Monto'].sum()

# 3. Configuración del gráfico
plt.figure(figsize=(8, 8))
colores = sns.color_palette('pastel')[0:len(ventas_por_producto)]

# 4. Crear el gráfico de torta
# autopct='%1.1f%%' sirve para mostrar el porcentaje con un decimal
plt.pie(ventas_por_producto, 
        labels=ventas_por_producto.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colores,
        explode=(0.1, 0, 0, 0)) # Separamos un poco la primera rebanada (Laptop) para destacar

plt.title('Participación por Producto en las Ventas Totales', fontsize=14)

# 5. Mostrar el resultado
plt.show()