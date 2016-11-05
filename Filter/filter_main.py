import cv2
from add_noise import *

from matplotlib import pyplot as plt
import numpy as np

# load image
cat = cv2.imread('catcon.png')
cat = cv2.cvtColor(cat,cv2.COLOR_BGR2GRAY)

# add noise
result = add_gaussian_noise(cat)

# display result
index = 0
for r in result:
    cv2.imshow('result'+str(index),r)
    index+=1
cv2.waitKey()