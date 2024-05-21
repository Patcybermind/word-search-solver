import cv2
import numpy as np
import pytesseract
import ocr
img = cv2.imread("images/image.png")
ocr.get_letters(img)