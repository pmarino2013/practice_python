import cv2

# 1. Preparación
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('../archivo/people.jpg')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- CONFIGURACIÓN A: PERMISIVA (Muchos falsos positivos) ---
# minNeighbors bajo (3) y sin tamaño mínimo
rostros_a = face_cascade.detectMultiScale(gris, 1.1, 3)

# --- CONFIGURACIÓN B: ESTRICTA (Filtrando errores) ---
# Subimos minNeighbors a 10 y pedimos un tamaño mínimo de 50x50
rostros_b = face_cascade.detectMultiScale(gris, 1.1, 10, minSize=(50, 50))

# 2. Dibujamos los resultados para comparar
img_resultado = img.copy()

# En ROJO los hallazgos del detector permisivo
for (x, y, w, h) in rostros_a:
    cv2.rectangle(img_resultado, (x, y), (x+w, y+h), (0, 0, 255), 2)

# En VERDE los hallazgos del detector estricto
for (x, y, w, h) in rostros_b:
    cv2.rectangle(img_resultado, (x, y), (x+w, y+h), (0, 255, 0), 3)

# 3. Mostrar leyenda y resultado
cv2.putText(img_resultado, "Rojo: Permisivo | Verde: Estricto", (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

cv2.imshow('Comparativa de Filtros', img_resultado)
cv2.waitKey(0)