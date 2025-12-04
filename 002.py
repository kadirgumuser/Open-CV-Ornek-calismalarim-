import cv2

img = cv2.imread('kadir.jpg')

resized = cv2.resize(img, (800, 600))

cv2.imshow("img", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
