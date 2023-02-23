import cv2
import numpy as np

# Cargar la imagen en escala de grises
img = cv2.imread('rick.jpg', cv2.IMREAD_GRAYSCALE)

# Definir el kernel para el filtro de detección de bordes
kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# Aplicar la convolución con el kernel
img_bordes = cv2.filter2D(img, -1, kernel)

# Mostrar la imagen original y la imagen con los bordes resaltados
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen con bordes', img_bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
