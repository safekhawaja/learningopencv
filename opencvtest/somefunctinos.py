import cv2
import numpy as np

img = cv2.imread("Resources/lads.png")
print(img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

cv2.imshow("Gray Lads", imgGray)
cv2.imshow("Blurred Lads", imgBlur)

imgCanny = cv2.Canny(img,150,200)
cv2.imshow("Canny Lads", imgCanny)

kernel = np.ones((5,5),np.uint8)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("Dilated Lads", imgDilation)

imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
cv2.imshow("Eroded Lads", imgEroded)

cv2.waitKey(0)