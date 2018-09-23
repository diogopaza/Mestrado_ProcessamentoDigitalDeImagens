import cv2

imagem = cv2.imread('sonic.jpg')
"""
print( imagem.shape )
print ( imagem.item( 0, 0, 2), imagem.item( 0, 0, 1), imagem.item( 0, 0, 0)  )
imagem.itemset( (0,0,2), 255 )
imagem.itemset( (0,0,1), 0 )
imagem.itemset( (0,0,0), 0 )
cv2.imwrite('sonic2.jpg', imagem)
cv2.imshow('minha_imagem', bola)

#cv2.imshow('minha_imagem', imagem)
bola = imagem[245:308, 220:280 ]
cv2.imwrite("bola.jpg",bola)
imagem[ 179:242 ,235:295] = bola
cv2.imwrite('soccer3.jpg', imagem)

"""
print ( imagem.item( 33, 69, 2), imagem.item( 33, 69, 1), imagem.item( 33, 69, 0)  )

#cv2.imshow('minha_imagem', imagem)
