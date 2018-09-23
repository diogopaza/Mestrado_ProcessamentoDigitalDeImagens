import cv2

imagem_carregada = cv2.imread('sonic.jpg', 2)

cv2.imshow("Imagem", imagem_carregada)
cv2.waitKey(0)# tempo de espera para fechar a janela
cv2.destroyAllWindows()#fecha todas as janelas abertas

cv2.imwrite("imagem_salva.jpg", imagem_carregada)
