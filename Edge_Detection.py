import cv2
import numpy as np


image = cv2.imread("input/spider.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result = np.zeros(image.shape)

mask = np.array([[-1, -1, -1],
                 [-1, 8, -1],
                 [-1, -1, -1]])


rows, cols = image.shape

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_image = image[i-1:i+2 , j-1:j+2]
        result[i, j] = np.sum(small_image * mask)

cv2.imwrite("output/Result_Spider.jpg", result)
cv2.imshow('', result)
cv2.waitKey()