
import cv2

img = cv2.imread("jogador.jpg")
imgYCC = cv2.cvtColor( img, cv2.COLOR_BGR2YCrCb)

imgNova =  imgYCC[:,:,2] 
cv2.imshow('Ycbcr', imgNova)
