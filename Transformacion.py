import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('rick.jpg')

# Escalar la imagen
img_scaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# Rotar la imagen
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
img_rotated = cv2.warpAffine(img, M, (cols, rows))

# Trasladar la imagen
M = np.float32([[1, 0, 50], [0, 1, 50]])
img_translated = cv2.warpAffine(img, M, (cols, rows))

# Mostrar las imágenes resultantes
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen escalada', img_scaled)
cv2.imshow('Imagen rotada', img_rotated)
cv2.imshow('Imagen trasladada', img_translated)
cv2.waitKey(0)
cv2.destroyAllWindows()