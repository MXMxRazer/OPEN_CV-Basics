import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("Blank", blank)

# Paint a color
blank[200:300, 300:400] = 0, 255, 0
# cv.imshow("Green", blank)

# Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=cv.FILLED)
# cv.imshow("Rectangle", blank)

# Draw a cricle
cv.circle(
    blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (255, 0, 0), thickness=-1
)
# cv.imshow("Circle", blank)

# Draw a line
cv.line(blank, (100, 100), (400, 400), (255, 0, 0), thickness=20)
# cv.imshow("Line", blank)

# Write text
cv.putText(
    blank, "Hello, World", (10, 80), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2
)
cv.imshow("Text", blank)

cv.waitKey(0)
