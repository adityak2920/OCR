import cv2
import sys
import pytesseract
import urllib.request
import numpy as np

# IP address from ipwebcam app
url = "http://192.168.43.1:8080/shot.jpg"

while True:
    # Extracting from url and converting it to image format so that opencv can read
    img_response = urllib.request.urlopen(url)
    img_numpy = np.array(bytearray(img_response.read()), dtype=np.uint8)
    frame = cv2.imdecode(img_numpy, -1)
    config = ('-l eng --oem 1 --psm 3')

    # Read image for OCR
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Run tesseract OCR on image
    text = pytesseract.image_to_string(gray, config=config)

    # Print recognized text
    print(text)
    
    # Displaying the video
    cv2.imshow('IPWebcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
