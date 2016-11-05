import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg')
plt.imshow(img)
plt.show()