import cv2

cap = cv2.VideoCapture(0)   # 0 = varsayılan kamera

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare okunamadı!")
        break

    cv2.imshow("Kamera", frame)

    # 'q' tuşuna basınca çıkış
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
