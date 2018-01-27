import cv2
import numpy as np 

class Filter():

    def snow(img, pointNumber, pointColor):
        for k in range(pointNumber):
            i = int(np.random.random() * img.shape[0])
            j = int(np.random.random() * img.shape[1])

            if img.ndim == 2:
                img[i, j] = pointColor
            
            if img.ndim == 3:
                img[i, j, 0] = pointColor
                img[i, j, 1] = pointColor
                img[i, j, 2] = pointColor

        return img


