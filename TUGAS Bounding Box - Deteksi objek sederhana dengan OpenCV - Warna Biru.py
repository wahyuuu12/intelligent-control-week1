import cv2
import numpy as np
# Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
# Rentang warna biru dalam HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([100, 150, 70]), np.array([140, 255, 255]))
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Deteksi kontur dari objek biru
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # Filter ukuran minimum kontur
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Biru", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
     # Menampilkan hasil
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()