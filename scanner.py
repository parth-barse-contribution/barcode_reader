import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(1)
cap.set(3, 420)
cap.set(4, 280)

cam = True

img = cv2.imread("barcode4.jpeg")

while cam == True:
    s, frame = cap.read()
    
    cv2.imshow("", frame)
    cv2.waitKey(1)

    decoding_info = decode(frame)
    if decoding_info:
        print(decoding_info[0].data.decode())
        cam = False