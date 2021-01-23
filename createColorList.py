def createColorList(startColor, endColor, steps):
    rDiff = endColor[0] - startColor[0]
    gDiff = endColor[1] - startColor[1]
    bDiff = endColor[2] - startColor[2]
    colorList = []
    for i in range(steps):
        factor = i/steps
        colorList.append([startColor[0] + factor*rDiff, startColor[1] + factor*gDiff, startColor[2] + factor*bDiff])
    return colorList