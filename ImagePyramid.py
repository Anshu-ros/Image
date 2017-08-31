import cv2
import numpy as np,sys
A = cv2.imread('Anshu.jpg')
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

ls = gpA[0]
for i in xrange(1,6):
    ls = cv2.pyrUp(ls)

cv2.imwrite('Pyramid.jpg',ls)
                 
