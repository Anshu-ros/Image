import cv2
import numpy as np,sys

image = cv2.imread('Anshu'.jpg)
G=image.copy()
G=cv2.pyrDown(G)
cv2.imwrite('Pyramid.jpg',G)
                 
