import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)

# draw circle
cv2.circle(img=img,center=(400,400),color=(0,0,255),radius=100, thickness=-1)

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()




print img[100,100]


if cv2.waitKey() == ord('s'):
# write an image
    cv2.imwrite('catcopy.png',img);
    print 'saved image'
else:
    cv2.destroyAllWindows();