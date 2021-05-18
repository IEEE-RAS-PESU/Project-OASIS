# -*- coding: utf-8 -*-
"""Generate and Detect QR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-3zICx2on3pON_h9dyeRbj1NKsKDcHq2
"""

pip install qrcode

import qrcode

import cv2

from google.colab.patches import cv2_imshow

img=qrcode.make("Hey this is MAHIMA DUBEY!!")

print(img.size)

print(type(img))

img.save('/content/test.png')

image=cv2.imread('/content/test.png')

cv2_imshow(image)

detector=cv2.QRCodeDetector()

data, bbox, straight_qr=detector.detectAndDecode(image)

print("Detected data=>",data)

print(bbox)

print(straight_qr)

