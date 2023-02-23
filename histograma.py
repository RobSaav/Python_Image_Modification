import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
img = cv2.imread('rick.jpg', 0)

# Calcular el histograma de la imagen
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# Mostrar el histograma
plt.plot(hist)
plt.title('Histograma de la imagen')
plt.xlabel('Niveles de gris')
plt.ylabel('Frecuencia')
plt.show()
