import numpy as np
import cv2

img = cv2.imread('images/cat.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):        
        sum = 0
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                sum = sum + a
        b = int(sum / 49.0)
        img_out.itemset((i,j), b)

cv2.imwrite('images/filter_box.jpg', img_out)

cv2.imshow('image',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()