import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('4x6.png')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (0,0,700,1100)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,iterCount=10,mode=cv2.GC_INIT_WITH_RECT)

# 0: background
# 1: foreground
# 2: probably background
# 3: probably foreground
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.show()