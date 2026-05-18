import cv2

# 1. Cargar la imagen
img = cv2.imread('test.png')

# 2. Convertir a escala de grises (procesamiento base de IA)
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Obtener dimensiones dinámicamente
# .shape nos da (alto, ancho, canales). Usamos indexación para el centro.
alto, ancho = img.shape[:2]
centro_x = ancho // 2
centro_y = alto // 2

# 4. Dibujar el "Ojo de Seguridad" (Círculo Rojo)
# cv2.circle(imagen, centro, radio, color_BGR, grosor)
cv2.circle(img, (centro_x, centro_y), 35, (0, 0, 255), 3)

# 5. Agregar una mira telescópica (opcional para estilo)
cv2.line(img, (centro_x - 50, centro_y), (centro_x + 50, centro_y), (0, 0, 255), 1)
cv2.line(img, (centro_x, centro_y - 50), (centro_x, centro_y + 50), (0, 0, 255), 1)

# 6. Mostrar resultado
cv2.imshow('Filtro de Seguridad Activado', img)
cv2.waitKey(0)
cv2.destroyAllWindows()