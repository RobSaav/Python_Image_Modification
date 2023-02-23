import cv2

# Cargar la imagen
img = cv2.imread('rick.jpg')

# Convertir a escala de grises
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización
threshold_value = 128
max_value = 255
ret, img_thresholded = cv2.threshold(img_gray, threshold_value, max_value, cv2.THRESH_BINARY)

# Aplicar la segmentación
contours, hierarchy = cv2.findContours(img_thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 0, 255), 3)

# Mostrar las imágenes resultantes
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen umbralizada', img_thresholded)
cv2.imshow('Imagen con contornos', img_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()