import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)
img[200:300,300:400] = 255,0,0

#shapes
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),cv2.FILLED)

#text
cv2.putText(img," OPENCV ",(300,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),1)

cv2.imshow("Image", img)

cv2.waitKey(0)