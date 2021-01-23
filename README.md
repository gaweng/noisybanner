# noisybanner
This Python-Script creates an Image. Cluster colored Text on noisy Background

## Example call
Required Parameters:
msg - Text, that should be displayed
font - URI to TTF-File
fontsize - fontsize in pt
imageSize - as tuple
colorRange - as tuple requires startColor(tuple), endColor(tuple), steps(int)

createBanner(
    "gtan", 
    "https://raw.githubusercontent.com/google/fonts/master/ofl/medievalsharp/MedievalSharp.ttf", 
    20, 
    (1440,300), 
    ((255,0,0),(255,255,0),12)
    )