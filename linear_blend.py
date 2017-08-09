import numpy as np
import cv2

img1 = cv2.imread('images/cat.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('images/lion.jpg', cv2.IMREAD_GRAYSCALE)

height = img1.shape[0]
width = img1.shape[1]

alpha = 0.5

for i in np.arange(height):
    for j in np.arange(width):
        a1 = img1.item(i,j)
        a2 = img2.item(i,j)
        b = alpha * a1 + (1-alpha) * a2
        img1.itemset((i,j), b)

cv2.imwrite('images/linear_blend.jpg', img1)

cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()