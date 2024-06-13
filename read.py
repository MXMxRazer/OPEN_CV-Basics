import cv2 as cv

# Image reading
# img = cv.imread("Photos/gitHub.png")

# cv.imshow("Profile", img)

# Video Reading
capture = cv.VideoCapture("Captures/video.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
