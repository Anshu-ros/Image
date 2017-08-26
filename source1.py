import numpy as np
import cv2
img=cv2.imread('Anshu.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('AnshuGray.jpg',img)
