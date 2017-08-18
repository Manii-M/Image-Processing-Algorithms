import numpy as np
import cv2
from matplotlib import pyplot as plt
from convolve_np import convolve_np

import edge_canny_get_orientation_sector as ors
import edge_canny_is_local_max as locmax
import edge_canny_trace_and_threshold as tt

img = cv2.imread('images/butterfly.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

# step 1: blur with Gaussian
gauss = (1.0/57) * np.array(
        [[0, 1, 2, 1, 0],
        [1, 3, 5, 3, 1],
        [2, 5, 9, 5, 2],
        [1, 3, 5, 3, 1],
        [0, 1, 2, 1, 0]])
img_blur = convolve_np(img, gauss)

# step 2: compute gradient magnitude
img_x = convolve_np(img_blur, np.array([[-0.5, 0, 0.5]]))
img_y = convolve_np(img_blur, np.array([[-0.5],
                                       [0],
                                       [0.5]]))
E_mag = np.sqrt(np.power(img_x, 2) + np.power(img_y, 2))
E_mag = (E_mag / np.max(E_mag)) * 255

# step 3: non-maximum suppression
t_low = 4
E_nms = np.zeros((height, width))
for i in np.arange(1, height-1):
    for j in np.arange(1, width-1):
        dx = img_x[i,j]
        dy = img_y[i,j]
        s_theta = ors.get_orientation_sector(dx,dy)
        
        if locmax.is_local_max(E_mag, i, j, s_theta, t_low):
            E_nms[i,j] = E_mag[i,j]

#step 4: edge tracing and hysteresis thresholding
t_high = 15
E_bin = np.zeros((height, width))
for i in np.arange(1, height-1):
    for j in np.arange(1, width-1):
        if E_nms[i,j] >= t_high and E_bin[i,j] == 0:
            tt.trace_and_threshold(E_nms, E_bin, i, j, t_low)

cv2.imwrite('images/edge_canny.jpg', E_bin)

plt.imshow(E_bin, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()