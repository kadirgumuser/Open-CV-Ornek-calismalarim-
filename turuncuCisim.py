import cv2
import numpy as np

# Kamerayı aç
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # BGR → HSV dönüşümü
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Turuncu için HSV aralığı
    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([25, 255, 255])

    # Maske oluştur
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Morfolojik işlemler
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Göster
    cv2.imshow("Original", frame)
    cv2.imshow("Orange Mask", mask)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
