import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg')

# from 450 to 1050 = 600px
# from 90 to 400 = 310px

# get the cat face
catface = img[100:500, 700:1100]
img[0:catface.shape[0],0:catface.shape[1]] = catface
print(catface.shape)
#plt.imshow(img);
#plt.show();

# our cat face
# cv2.imwrite('catface.png', catface)

# create border for cat
catface = cv2.copyMakeBorder(catface,value=(100,181,246),top=10,bottom=10,left=10,right=10,borderType=cv2.BORDER_CONSTANT)
catface = cv2.copyMakeBorder(catface,value=(66,165,245),top=10,bottom=10,left=10,right=10,borderType=cv2.BORDER_CONSTANT)
catface = cv2.copyMakeBorder(catface,value=(33,150,243),top=10,bottom=10,left=10,right=10,borderType=cv2.BORDER_CONSTANT)

cv2.imwrite('catface.png',catface)
plt.imshow(catface)
plt.show()