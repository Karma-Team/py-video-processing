import numpy as np

def HeatMap(image, size, colorMap):
    inShape = image.shape
    if len(inShape) > 2:
        raise TypeError("Image not in gray scale")

    outImage = np.empty((inShape[0], inShape[1], 3), dtype=np.uint8)
    outArray = np.empty((int(inShape[0]/size), int(inShape[1]/size)), dtype=np.uint8)

    for hI in range(int(inShape[0]/size)):
        for vI in range(int(inShape[1]/size)):
            score = np.sum(image[hI*size:(hI+1)*size , vI*size:(vI+1)*size]) / (size*size)
            outArray[hI, vI] = score

            colorIndex = np.searchsorted(colorMap[0], score)
            if colorIndex == len(colorMap[0]):
                colorScore = colorMap[1][colorIndex-1]
            elif colorIndex == 0:
                colorScore = colorMap[1][0]
            else:
                cursor = (1.0*score - colorMap[0][colorIndex-1])/(colorMap[0][colorIndex] - colorMap[0][colorIndex-1])
                colorScore = (1-cursor)*np.array(colorMap[1][colorIndex-1]) + cursor*np.array(colorMap[1][colorIndex])
            
            outImage[hI*size:(hI+1)*size , vI*size:(vI+1)*size, :] = np.array(colorScore)

    return (outImage, outArray)

