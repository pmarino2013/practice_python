import cv2

# 1. Cargamos ambos clasificadores (Rostros y Sonrisas)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# 2. Leer la imagen y pasarla a gris
img = cv2.imread('../archivo/personas_mayores.jpg')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Detectar rostros primero (Filtro estricto para evitar errores)
rostros = face_cascade.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=8, minSize=(70, 70))

for (x, y, w, h) in rostros:
    # Dibujamos el rectángulo AZUL para el rostro
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(img, 'Rostro', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    
    # --- AQUÍ ESTÁ EL TRUCO: Definimos la Región de Interés (ROI) ---
    # Recortamos el rostro en la imagen gris (para la IA) y en la imagen a color (para dibujar)
    roi_gris = gris[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    # 4. Buscamos la sonrisa SOLO dentro del cuadro del rostro
    # Nota: Usamos un minNeighbors alto (20 o más) porque las sonrisas fallan fácil
    sonrisas = smile_cascade.detectMultiScale(roi_gris, scaleFactor=1.5, minNeighbors=16, minSize=(25, 25))
    
    for (sx, sy, sw, sh) in sonrisas:
        # Dibujamos el rectángulo VERDE para la sonrisa
        # ¡Ojo! Dibujamos sobre 'roi_color' usando las coordenadas de la sonrisa (sx, sy)
        cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
        cv2.putText(roi_color, 'Feliz', (sx, sy-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# 5. Mostrar el resultado final
cv2.imshow('Detector de Felicidad Academico', img)
cv2.waitKey(0)
cv2.destroyAllWindows()