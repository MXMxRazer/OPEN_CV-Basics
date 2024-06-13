import cv2 as cv
import numpy as np

img = cv.imread("Photos/gitHub.png")
cv.imshow("Profile", img)


# Translation of an image
# => Shifting image in any axis
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# Directions for the values of x and y
# - x => Left
# - y => up
# x => right
# y => down
translated = translate(img, 100, 100)
# cv.imshow("Translated", translated)


# Rotation of an image
def rotate(img, angle, rotPoint=None):
    height, width = img.shape[:2]

    if rotPoint == None:
        rotPoint = width // 2, height // 2

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = width, height

    return cv.warpAffine(img, rotMat, dimensions)


# Rotation directions
# pos = anti-clock-wise
# neg = clock-wise

rotated = rotate(img, 45)
# cv.imshow("Rotated", rotated)

# Flipping of an image
# 0 => Y-axis
# 1 => X-axis
# - 1 => X/Y-axis
flip = cv.flip(img, -1)
cv.imshow("Flipped", flip)

cv.waitKey(0)
