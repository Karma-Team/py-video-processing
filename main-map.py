import numpy as np
import cv2

FILENAME = "capture.png"
THRESHOLD_RED = 50 #  127
THRESHOLD_GREEN = 60 #  127
THRESHOLD_V = 30 #  127

BLUE = 0
RED = 1
GREEN = 2
H = 0
S = 1
V = 2

img = cv2.imread(FILENAME)
dimY, dimX, _ = img.shape
print(dimX, dimY)

imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("init", img)
cv2.imshow("grey", imgg)

# Up and down board limit

deriveImgX = imgg[:-1, :] - imgg[1:, :]
deriveImgY = imgg[:, :-1] - imgg[:, 1:]


cv2.imshow("deriveImgX", deriveImgX)

lineScoreX = deriveImgX.sum(axis=1)
UpYLine = np.argmax(lineScoreX[:dimY // 2])
DownYLine = np.argmax(lineScoreX[dimY // 2:]) + dimY // 2

print("UpXline", UpYLine, "DownYLine", DownYLine, "mid", dimX // 2)

# Find contours
posOrigin = ((3 * dimX) // 4 - 30, UpYLine)
posOrigin = (237, UpYLine)

COEFF = 3
COEFF_OUTSIDE = 1
OFFSET_OUTSIDE = -255
COEFF_MIDDLE = -0.5
OFFSET_MIDDLE = 125
COEFF_INSIDE = -1
OFFSET_INSIDE = 255
OFFSET_MAT = [[(COEFF_INSIDE, OFFSET_INSIDE), (COEFF_MIDDLE, OFFSET_MIDDLE), (COEFF_OUTSIDE, OFFSET_OUTSIDE)],
              [(COEFF_MIDDLE, OFFSET_MIDDLE), (COEFF_INSIDE, OFFSET_INSIDE), (COEFF_MIDDLE, OFFSET_MIDDLE)],
              [(COEFF_OUTSIDE, OFFSET_OUTSIDE), (COEFF_MIDDLE, OFFSET_MIDDLE), (COEFF_INSIDE, OFFSET_INSIDE)]]

def angle_detection(img, posOrigin, dir, verbose=False):
    origin = int(img[posOrigin[1], posOrigin[0]])
    score = 0
    if verbose:
        scoreMat = []
        scoreAbs = []
    for x in range(3):
        if verbose:
            scoreX = []
            scoreXAbs = []
        for y in range(3):
            point = int(img[posOrigin[1] + x*dir, posOrigin[0] + y])
            scorePts = (abs(origin - point) * OFFSET_MAT[x][y][0]) + OFFSET_MAT[x][y][1]
            if verbose:
                scoreX.append(scorePts)
                scoreXAbs.append(abs(origin - point))
            score += scorePts
        if verbose:
            scoreMat.append(scoreX)
            scoreAbs.append(scoreXAbs)
    if verbose:
        for s in scoreMat:
            print("{: 3} {: 3} {: 3}".format(*s))
        print("---")
        for s in scoreAbs:
            print("{: 3} {: 3} {: 3}".format(*s))
    return score

test = angle_detection(deriveImgX, posOrigin, -1, True)
print(posOrigin, test)
scoreRight = [angle_detection(deriveImgX, (x, UpYLine), 1) for x in range(2*dimX//3, dimX - 5)]
scoreLeft = [angle_detection(deriveImgX, (x, UpYLine), -1) for x in range(0, dimX//3)]
posMaxScoreRight = np.argmax(scoreRight) + 2*dimX//3
maxScoreRight = scoreRight[np.argmax(scoreRight)]
posMaxScoreLeft = np.argmax(scoreLeft)
maxScoreLeft = scoreLeft[posMaxScoreLeft]
scoreRight = [(255 * s) / maxScoreRight for s in scoreRight]
scoreLeft = [(255 * s) / maxScoreLeft for s in scoreLeft]

print("Left", posMaxScoreLeft, maxScoreLeft)

# Follow Line
def max_move(img, posOrigin, dir):
    origin = int(img[posOrigin[1], posOrigin[0]])
    pts1 = int(img[posOrigin[1] + 2, posOrigin[0] + 1*dir])
    pts2 = int(img[posOrigin[1] + 2, posOrigin[0] + 2*dir])
    pts3 = int(img[posOrigin[1] + 1, posOrigin[0] + 2*dir])
    diff1 = abs(origin - pts1)
    diff2 = abs(origin - pts2)
    diff3 = abs(origin - pts3)
    argM = np.argmin([diff1, diff2, diff3])
    if argM == 0:
        return posOrigin[0] + 1*dir, posOrigin[1] + 2
    elif argM == 0:
        return posOrigin[0] + 2*dir, posOrigin[1] + 2
    else:
        return posOrigin[0] + 2*dir, posOrigin[1] + 1

posOriginRight = (posMaxScoreRight, UpYLine)
while posOriginRight[0] < dimX - 2:
    posOriginRight = max_move(deriveImgX, posOriginRight, 1)

posOriginLeft = (posMaxScoreLeft, UpYLine)
while posOriginLeft[0] > 0 + 2:
    posOriginLeft = max_move(deriveImgX, posOriginLeft, -1)



# Print output

# deriveImgYBGR = cv2.cvtColor(deriveImgY, cv2.COLOR_GRAY2BGR)
# deriveImgYLine = cv2.line(deriveImgYBGR, (0, UpXLine), (dimY, UpXLine), (0, 0, 255), 1)
# cv2.imshow("deriveImgYLine", deriveImgYLine)

deriveImgXBGR = cv2.cvtColor(deriveImgX, cv2.COLOR_GRAY2BGR)

imgLine = cv2.line(img, (0, UpYLine), (dimX, UpYLine), (0, 0, 255), 1)
deriveImgXBGRLine = cv2.line(deriveImgXBGR, (0, UpYLine), (dimX, UpYLine), (0, 0, 255), 1)
imgLine = cv2.line(imgLine, (0, DownYLine), (dimX, DownYLine), (0, 0, 255), 1)
deriveImgXBGRLine = cv2.line(deriveImgXBGRLine, (0, DownYLine), (dimX, DownYLine), (0, 0, 255), 1)

for x in range(2*dimX//3, dimX - 5):
    deriveImgXBGRLine = cv2.line(deriveImgXBGR, (x, UpYLine), (x, UpYLine), (0, scoreRight[x - 2*dimX//3], 0), 1)
for x in range(0, dimX//3):
    deriveImgXBGRLine = cv2.line(deriveImgXBGR, (x, UpYLine), (x, UpYLine), (0, scoreLeft[x], 0), 1)

deriveImgXBGRLine = cv2.circle(deriveImgXBGRLine, center=(posMaxScoreLeft, UpYLine), radius=5, color=(255,255,0), thickness=1)
deriveImgXBGRLine = cv2.circle(deriveImgXBGRLine, center=(posMaxScoreRight, UpYLine), radius=5, color=(255,255,0), thickness=1)
#deriveImgXBGRLine = cv2.circle(deriveImgXBGRLine, center=posOrigin, radius=6, color=(0,255,255), thickness=1)

deriveImgXBGRLine = cv2.circle(deriveImgXBGRLine, center=posOriginRight, radius=5, color=(255,0,255), thickness=1)
deriveImgXBGRLine = cv2.circle(deriveImgXBGRLine, center=posOriginLeft, radius=5, color=(255,0,255), thickness=1)


cv2.imshow("imgLine", imgLine)
cv2.imshow("deriveImgXBGRLine", deriveImgXBGRLine)





cv2.waitKey(0)

cv2.destroyAllWindows()
