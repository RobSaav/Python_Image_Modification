import cv2
import numpy as np

# Cargar imagen de ejemplo
img = cv2.imread('rick.jpg')

# Definir puntos de la región de interés
roi_points = np.array([(50, 50), (400, 50), (400, 400), (50, 400)], np.int32)

# Crear una máscara a partir de la región de interés
mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.fillPoly(mask, [roi_points], 255)

# Aplicar segmentación a la imagen para separar la región de interés del fondo
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Definir puntos para la transformación de perspectiva
src_points = np.float32([(50, 50), (400, 50), (400, 400), (50, 400)])
dst_points = np.float32([(0, 0), (300, 0), (300, 300), (0, 300)])

# Calcular la matriz de transformación
M = cv2.getPerspectiveTransform(src_points, dst_points)

# Aplicar la transformación de perspectiva a la región de interés
result = cv2.warpPerspective(masked_img, M, (300, 300))

# Mostrar la imagen resultante
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()