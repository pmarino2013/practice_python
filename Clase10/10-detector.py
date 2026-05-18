# import cv2
# import os

# # 1. Construimos rutas absolutas desde el directorio del script
# base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'archivo'))
# cascade_path = os.path.join(base_dir, 'haarcascade_frontalface_default.xml')
# img_path = os.path.join(base_dir, 'people.jpg')

# if not os.path.exists(cascade_path):
#     raise FileNotFoundError(f'No se encontró el clasificador: {cascade_path}')
# if not os.path.exists(img_path):
#     raise FileNotFoundError(f'No se encontró la imagen: {img_path}')

# # 2. Cargamos el clasificador (el "modelo" ya entrenado)
# face_cascade = cv2.CascadeClassifier(cascade_path)
# if face_cascade.empty():
#     raise RuntimeError(f'Error al cargar el clasificador de rostros: {cascade_path}')

# # 3. Cargamos la imagen y la convertimos a gris
# # (Recordá: la IA procesa mejor en gris porque hay menos ruido)
# img = cv2.imread(img_path)
# if img is None:
#     raise RuntimeError(f'Error al cargar la imagen: {img_path}')
# filtro_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 3. Buscamos los rostros
# # detectMultiScale devuelve una lista de rectángulos [x, y, ancho, alto]
# rostros = face_cascade.detectMultiScale(filtro_gris, 1.1, 4)
# print(rostros)

# # 4. Dibujamos un rectángulo sobre cada rostro detectado
# for (x, y, w, h) in rostros:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     cv2.putText(img, 'Humano Detectado', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

# # 5. Mostramos el resultado
# cv2.imshow('Sistema de Seguridad Academico', img)
# cv2.waitKey(0)
import cv2
import os
import subprocess

# 1. Cargamos el clasificador (el "modelo" ya entrenado) la librería ya lo trae incluido
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Cargamos la imagen y la convertimos a gris
# (Recordá: la IA procesa mejor en gris porque hay menos ruido)
img = cv2.imread('../archivo/personas_mayores.jpg')
filtro_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def limpiar_terminal():
    if os.name=='nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

#función para pasar parámetros 
def detected_face():
    limpiar_terminal()
    print("--- DETECTOR DE ROSTROS ---")
    zoom=input('1. Ingrese la escala de zoom (1.1 | 1.2 | 1.3): ') or 1.1
    calidad = input('2. Ingrese el valor del filtro de calidad (5 | 8 |10): ') or 8
    distancia = input('3. Ingresar filtro de distancia ( 50 | 70 | 200): ') or 70

    rostros = face_cascade.detectMultiScale(
    filtro_gris, 
    scaleFactor=float(zoom), 
    minNeighbors=int(calidad), 
    minSize=(int(distancia),int(distancia)) 
    )
    # 4. Dibujamos un rectángulo sobre cada rostro detectado
    for (x, y, w, h) in rostros:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, 'Humano Detectado', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    print('--- MOSTRANDO VENTANA DE IMAGEN ---')
    print("Presione una tecla para cerrar la ventana")

# 3. Buscamos los rostros
# detectMultiScale devuelve una lista de rectángulos [x, y, ancho, alto]
# rostros = face_cascade.detectMultiScale(filtro_gris, 1.1, 10)
# rostros = face_cascade.detectMultiScale(
#     filtro_gris, 
#     scaleFactor=1.1, 
#     minNeighbors=8, 
#     minSize=(70, 70) 
# )

# 4. Dibujamos un rectángulo sobre cada rostro detectado
# for (x, y, w, h) in rostros:
#     cv2.rectangle(filtro_gris, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     cv2.putText(filtro_gris, 'Humano Detectado', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

# 5. Mostramos el resultado
detected_face()
cv2.imshow('Sistema de Seguridad Academico', img)
cv2.waitKey(0)