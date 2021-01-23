import numpy as np
import random


def createNoisyImage(img, fgList, bgList, steps):
    img[img<255] = 0
    white = np.array([255,255,255])
    black = np.array([0,0,0])
    for x, xVal in enumerate(img):
        for y, yVal in enumerate(xVal):
            if (yVal == white).all():
                img[x,y] = bgList[random.randint(0,2)]
            elif(yVal == black).all():
                img[x-4:x+4, y-4:y+4] = fgList[random.randint(0, steps-1)]
    return img