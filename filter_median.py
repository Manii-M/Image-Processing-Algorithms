import numpy as np
import cv2

img = cv2.imread('images/plane_noisy.png', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):
        neighbors = []
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                neighbors.append(a)
        neighbors.sort()
        median = neighbors[24]
        b = median
        img_out.itemset((i,j), b)

cv2.imwrite('images/filter_median.jpg', img_out)

cv2.imshow('image',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()