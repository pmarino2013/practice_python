import cv2


imagen=cv2.imread('test.png')

gris= cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


#Cargo la imagen en la ventana
# cv2.imshow('Mi primera ventana OpenCV', imagen)

#cambiar a escala de grises
cv2.imshow('Mi primera ventana OpenCV', gris)

#guardar una copia de la imagen original en grises
cv2.imwrite('foto_gris.png', gris)



#Espera que presione una tecla para cerra la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()

