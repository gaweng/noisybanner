import numpy as np
from createTextImage import createTextImage
from createColorList import createColorList
from createNoisyImage import createNoisyImage
import matplotlib.pyplot as plt


# Example createBanner("gtan", "https://raw.githubusercontent.com/google/fonts/master/ofl/medievalsharp/MedievalSharp.ttf", 20, (1440,300), ((255,0,0),(255,255,0),12))
def createBanner(msg, font, fontsize, imageSize, colorRange):
    img = createTextImage(msg, font, fontsize, imageSize)

    # Color list for background noise
    bgList = [
        np.array([175, 175, 175]),
        np.array([200, 200, 200]),
        np.array([225, 225, 225])
    ]

    fgList = createColorList(colorRange[0], colorRange[1], colorRange[2])
    print(fgList)
    img = createNoisyImage(img, fgList, bgList, colorRange[2])

    plt.imsave("output.png",img)