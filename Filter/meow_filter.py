import cv2
import numpy as np


class Filter:
    def __init__(self, k):
        if (k%2 ==0):
            k+=1
        self.k = k
        self.mask = np.ones((k,k))

    def average_filter(self,img):
        result = np.copy(img)
        nrow = img.shape[0]
        ncol = img.shape[1]
        k = self.k
        n_window = k*k
        mid = k/2+1
        for r in range(1,nrow-k,2):
            for c in range(1,ncol-k,2):
                window = img[r:r+k,c:c+k]
                cat3 = window[1,1]
                s = 0
                for index in np.ndindex(k,k):
                    cell = window[index[0],index[1]]
                    s +=cell

                s /= n_window


                result_windows = result[r:r+k,c:c+k]
                # print (s,result_windows[mid,mid])
                result_windows[mid,mid] = s
        return result

