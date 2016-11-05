import cv2
from add_noise import *
from meow_filter import Filter

from matplotlib import pyplot as plt
import numpy as np

# load image
cat = cv2.imread('catcon.png')
cat = cv2.cvtColor(cat,cv2.COLOR_BGR2GRAY)
cat3 = cat[3,3]
print (type(cat))


# add noise
result = add_gaussian_noise(cat)
img0 = result[0]

# filter
my_filter = Filter(20)
result = my_filter.average_filter(cat)


# display result
index = 0
cv2.imshow('result',result)
cv2.imshow('original',cat)
#for r in result:
#   cv2.imshow('result'+str(index),r)
#   index+=1
cv2.waitKey()