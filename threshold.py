import numpy as np
import cv2

img = cv2.imread('images/low_contrast_1.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

threshold = 150

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        if a > threshold:
            b = 255
        else:
            b = 0
        img.itemset((i,j), b)

cv2.imwrite('images/threshold.jpg', img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()