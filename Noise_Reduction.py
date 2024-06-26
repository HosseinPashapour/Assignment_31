import numpy as np
import cv2

img = cv2.imread('Input/xray_noisy.png',cv2.IMREAD_GRAYSCALE)

def Noice_Reduction(img,n):
    kernel= np.ones((n,n)) / (n*n)
    rows , cols = img.shape
    result = np.zeros((rows,cols),dtype=np.uint8)

    t = (n-1) // 2
    for i in range(t , rows-t):
        for j in range(t , cols-t):
            small = img[i-t:i+t+1 , j-t:j+t+1]
            result[i,j] = np.sum(small*kernel)

    return result

result = Noice_Reduction(img,3)


cv2.imshow('',result)
cv2.waitKey()
cv2.imwrite('output/Result_xray_noisy.png', result)
