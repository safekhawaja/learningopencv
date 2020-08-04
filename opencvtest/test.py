import cv2

""" img = cv2.imread("Resources/lads.png")
cv2.imshow("Lads",img)
cv2.waitKey(10000)
"""

frameWidth = 1000
frameHeight = 772

cap = cv2.VideoCapture("Resources/intro.mov")
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("intro", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
