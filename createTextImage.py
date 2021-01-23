import numpy as np
from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen

def createTextImage(msg, fontUri, fontsize, imageSize):
    img = Image.new('RGB', imageSize, (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(getFont(fontUri), 200)
    w,h = font.getsize(msg)
    draw.text(((imageSize[0]-w)/2,(imageSize[1]-h)/2), msg, font=font, fill="black")
    return np.array(img)

def getFont(font):
    if ("http://" in font) or ("https://" in font):
        return urlopen(font)
    return font