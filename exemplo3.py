import cv2

imagem = cv2.imread('sonic.jpg')
print( imagem.shape )
print ( imagem.item( 0, 0, 2), imagem.item( 0, 0, 1), imagem.item( 0, 0, 0)  )
