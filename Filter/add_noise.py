import cv2
from matplotlib import pyplot as plt
import numpy as np


def add_gaussian_noise(img, range=(0,100)):

    # add noise
    print (img.shape)

    size = img.shape
    noise = np.random.randint(range[0],range[1],size,'uint8')

    print (noise.dtype)
    print (img.dtype)

    cat_noisecv = cv2.add(img, noise)
    cat_noisenp = img + noise
    return (cat_noisenp,cat_noisecv)