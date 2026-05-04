import pandas as pd
import os

# 1. Crear un dataset de ejemplo para la práctica
# data = {
#     'Vendedor': ['Ana', 'Pedro', 'Ana', 'Luis', 'Pedro', 'Ana'],
#     'Producto': ['Laptop', 'Mouse', 'Monitor', 'Laptop', 'Teclado', 'Mouse'],
#     'Monto': [1200, 25, 300, 1100, 45, 25],
#     'Fecha': ['2026-01-05', '2026-01-07', '2026-02-10', '2026-02-15', '2026-03-01', '2026-03-05']
# }

# df = pd.DataFrame(data)
df = pd.read_csv('archivo/ventas.csv')

print(df.info())

# 2. Análisis del negocio
print("--- Resumen Estadístico ---")
print(df.describe())

# 3. ¿Quién vendió más en total?
ventas_por_persona = df.groupby('Vendedor')['Monto'].sum()
print("\n--- Ventas Totales por Vendedor ---")
print(ventas_por_persona)

# 4. Filtrar ventas grandes

ventas_pro = df[df['Monto'] > 500]

# 5. Guardar el reporte en un nuevo archivo

ventas_pro.to_csv("reporte_ventas_pro.csv", index=False)
print("\n✅ Reporte generado: reporte_ventas_pro.csv")

# count     6.000000 Contar el número de observaciones que no son NA/nulas.
# mean    449.166667 Promedio.
# std     553.673339 Desviación estándar de las observaciones.
# min      25.000000 mínimo
# 25%      30.000000 
# 50%     172.500000
# 75%     900.000000
# max    1200.000000