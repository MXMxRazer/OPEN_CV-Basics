import cv2 as cv
import numpy as np

img = cv.imread("./Photos/gitHub.png")
cv.imshow("image", img)

# Averaging Blur
average = cv.blur(img, (3, 3))
cv.imshow("Average Blur", average)

# Gaussian Blur => more natural
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gaussian)

# Median Blur => more effective in reducing noise
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral Blur => most effective in reducing noise (retains the edges)
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)
