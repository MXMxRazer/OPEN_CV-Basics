import cv2 as cv

# Image reading
img = cv.imread("Photos/gitHub.png")
# cv.imshow("Profile", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholding", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholding Inverse", thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3
)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)
