import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'banana.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)


# make the line thicker for visualize
dst = cv2.dilate(dst,None)
img[dst>0.01*dst.max()]=[255,0,0]


plt.imshow(dst)
plt.show()
