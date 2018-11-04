
import cv2

img = cv2.imread("jogador.jpg")
imgYCC = cv2.cvtColor( img, cv2.COLOR_BGR2YCrCb)

imgVoltaBGR = cv2.cvtColor( imgYCC, cv2.COLOR_YCR_CB2BGR)
#imgNova =  imgYCC[:,:,0]

n=2
imgNormal = imgYCC[:,:,0],imgYCC[:,:,1],imgYCC[:,:,2]

cv2.imshow('novaImagem', imgNormal )



#exibi imagem em Ycbcr
#cv2.imshow('Ycbcr', imgYCC)
#exibi imagem em RGB
#cv2.imshow('volta rbg', imgVoltaBGR)
