import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('rick.jpg')

# Crear una máscara con un rectángulo blanco en el centro
mascara = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.rectangle(mascara, (200, 200), (400, 400), (255, 255, 255), -1)

# Aplicar la máscara a la imagen
img_con_mascara = cv2.bitwise_and(img, img, mask=mascara)

# Mostrar la imagen original y la imagen con la máscara aplicada
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen con máscara', img_con_mascara)
cv2.waitKey(0)
cv2.destroyAllWindows()
