import cv2

img = cv2.imread("Resources/lads.png")
print(img.shape)

imgResize = cv2.resize(img, (800, 900))
print(imgResize.shape)

imgCropped = img[100:700,200:700]

cv2.imshow("Image", img)
cv2.imshow("ImageR", imgResize)
cv2.imshow("ImageC", imgCropped)

cv2.waitKey(0)