import cv2

imagem = cv2.imread("imagem_trabalho.jpg")
imagemFinal = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem', imagemFinal)
