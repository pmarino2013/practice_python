import cv2

imagen = cv2.imread('test.png')

# Dibujar un rectángulo: (imagen, punto1, punto2, color BGR, grosor)
cv2.rectangle(imagen, (50,50), (200, 200), (0, 255, 0), 3)

# Poner texto: (imagen, texto, posicion, fuente, escala, color, grosor)
cv2.putText(imagen, "Objeto Detectado", (50, 40), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow('Deteccion Simulada', imagen)
cv2.waitKey(0)