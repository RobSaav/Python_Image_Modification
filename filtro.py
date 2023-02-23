import cv2

# Cargar la imagen
img = cv2.imread('rick.jpg')

# Aplicar un filtro gaussiano
img_suavizada = cv2.GaussianBlur(img, (5, 5), 0)

# Mostrar la imagen original y la imagen suavizada
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen suavizada', img_suavizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
