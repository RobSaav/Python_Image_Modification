import cv2

# Cargar la imagen en escala de grises
img_gray = cv2.imread('rick.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar la umbralización
umbral, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# Mostrar la imagen binaria resultante
cv2.imshow('Imagen binaria', img_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()


