import pandas as pd
import subprocess

subprocess.run("cls", shell=True)

# 1. CARGA DE DATOS
# Cargamos el archivo. Nota: Pandas intentará detectar las columnas automáticamente.
df = pd.read_csv('archivo/ventas.csv')
print("--- 1. Vista previa de los datos sucios ---")
print(df.head())
print(df.info())
print(df.describe())


# 2. LIMPIEZA (Data Wrangling)
# La última fila de Luis tiene valores NaN (Not a Number). Los eliminamos para no afectar las cuentas.
df_limpio = df.dropna()

# 3. TRANSFORMACIÓN DE FECHAS
# Convertimos la columna Fecha a formato datetime para que Python la entienda.
df_limpio['Fecha'] = pd.to_datetime(df_limpio['Fecha'], format='%m-%d-%y')

# 4. ANÁLISIS ESTADÍSTICO
total_ventas = df_limpio['Monto'].sum()
promedio_venta = df_limpio['Monto'].mean()
mejor_venta = df_limpio['Monto'].max()

print(f"\n--- 2. Resumen Ejecutivo ---")
print(f"Total Recaudado: ${total_ventas}")
print(f"Promedio por Venta: ${promedio_venta:.2f}") #dos decimales
print(f"Venta más alta: ${mejor_venta}")

#¿Quién vendió más en total?
ventas_por_persona = df_limpio.groupby('Vendedor')['Monto'].sum()
print("\n--- Ventas Totales por Vendedor ---")
print(ventas_por_persona)

# 5. SEGMENTACIÓN (Filtrado)
# Queremos ver solo las ventas "Premium" (mayores a 500)
ventas_premium = df_limpio[df_limpio['Monto'] > 500]

print("\n--- Ventas Premium Detectadas ---")
print(ventas_premium[['Vendedor', 'Producto', 'Monto']])

# 6. EXPORTACIÓN
# Guardamos el resultado limpio en un nuevo archivo para enviarlo al directorio.
ventas_premium.to_csv('reporte_premium.csv', index=False)
print("\n✅ Reporte 'reporte_premium.csv' generado con éxito.")

#TAREA DE ANALISIS DE FECHAS
# df["Fecha"]=pd.to_datetime(df["Fecha"], format="%m-%d-%y", errors="coerce")

# df["Año"]=df["Fecha"].dt.year

# print(df)