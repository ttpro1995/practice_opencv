import cv2
import numpy as np
from matplotlib import pyplot as plt

cat = cv2.imread('cat.jpg')
catsink = cv2.imread('catsink.jpg')
cat = cat[0:catsink.shape[0]] # resize to same size at catsink

# plus 2 cat np method
fusionCatnp = cat + catsink

# plus 2 cat cv2 method
fusionCatcv2 = cv2.add(cat,catsink)

# blend
blendCat = cv2.addWeighted(cat,0.5,catsink,0.5,0)

# display
plt.figure('add_numpy')
plt.imshow(fusionCatnp)

plt.figure('add cv2')
plt.imshow(fusionCatcv2)

plt.figure('blendcat')
plt.imshow(blendCat)

plt.show()

