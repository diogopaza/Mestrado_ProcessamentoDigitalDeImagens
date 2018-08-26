import cv2

imagemCarregada = cv2.imread("image.jpeg", 5)


cv2.imshow('ImagemCarregada', imagemCarregada)
#espera um tempo em segundos para fechar a janela.
cv2.waitKey(0)
cv2.destroyAllWindows()
