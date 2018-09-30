import numpy as np
import cv2

#le a imagem a partir de um arquivo
img = cv2.imread("jogador.jpg")
"""
Para reduzir a imagem, seleciona uma em cada duas colunas e uma
em cada duas linhas 
"""

n=2
img_reduzida= img[::n,::n]

"""
Agora a imagem é aumentada a partir da imagem reduzida, os pixel serão
duplicados no eixo x e y
Função nrepeat( imagem, vezes, eixo )
"""

m=2
img_aumentada = np.repeat( img_reduzida, m, axis=0)
img_aumentada = np.repeat( img_aumentada, m, axis=1)
cv2.imshow('aumentada', img_aumentada)

#grava imagem 
cv2.imwrite('img_aumentada.jpg', img_aumentada)


