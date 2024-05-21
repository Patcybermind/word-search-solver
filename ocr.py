
import cv2
import numpy as np
import pytesseract

# source of the get letters code: https://stackoverflow.com/questions/61327857/how-to-extract-individual-letters-from-image-with-pytesseract

def get_letters(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    items = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = items[0] if len(items) == 2 else items[1]

    img_contour = img.copy()
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if 100 < area < 10000:
            cv2.drawContours(img_contour, contours, i, (0, 0, 255), 2)

    detected = ""
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        ratio = h/w
        area = cv2.contourArea(c)
        base = np.ones(thresholded_image.shape, dtype=np.uint8)
        if ratio > 0.9 and 100 < area < 10000:
            base[y:y+h, x:x+w] = thresholded_image[y:y+h, x:x+w]
            segment = cv2.bitwise_not(base)

            custom_config = r'-l eng --oem 3 --psm 10 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ" '
            c = pytesseract.image_to_string(segment, config=custom_config)
            print(c)
            detected = detected + c
            cv2.imshow("segment", segment)
            cv2.waitKey(0)
        else:
            print("not detected\n")
            detected = detected + "ND\n"


    print("detected:\n" + detected)

    cv2.imshow("img_contour", img_contour)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    