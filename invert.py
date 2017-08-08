import numpy as np
import cv2

img = cv2.imread('images/low_contrast_1.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

max_intensity = 255

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        b = max_intensity - a
        img.itemset((i,j), b)

cv2.imwrite('images/invert.jpg', img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()