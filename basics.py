import cv2 as cv

img = cv.imread("Photos/gitHub.png")
cv.imshow("Profile", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayed", gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("Blurred", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow("Canny", canny)

# Dilate image
dilated = cv.dilate(canny, (3, 3), iterations=2)
# cv.imshow("Dilated", dilated)

# Erode image
eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow("Eroded", eroded)

# Resize image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)

# Crop image
cropped = img[20:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
