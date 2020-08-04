import cv2
import numpy as np

img = cv2.imread("Resources/lads.png")

width,height = 250,300
pts1 = np.float32([[420,440],[610,620],[420,620],[440,610]])
pts2 = np.float32([[0,0],[width,height],[0,width],[height,0]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)