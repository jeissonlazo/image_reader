import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Bostron", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# simple thresholding

threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)


threshold, thresh_inve = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold thresh_inve", thresh_inve)

# adaptive thresholding

adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5
)
cv.imshow("Adaptive Threshold", adaptive_thresh)
cv.waitKey(0)
