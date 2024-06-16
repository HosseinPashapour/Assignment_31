import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray_image], [0], None, [250], [0, 250])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

image = cv2.imread('input\Cats.jpeg')
hist = histogram(image)

plt.plot(hist)
plt.title('Histogram (plt.plot())')
plt.show()

plt.hist(image.ravel(), 250, [0, 250])
plt.title('Histogram (plt.hist())')
plt.show()

plt.bar(np.arange(250), hist)
plt.title('Histogram (plt.bar())')
plt.show()