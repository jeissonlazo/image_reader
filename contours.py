import cv2 as cv

img = cv.imread("Photos/cats.jpg")

cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

canny = cv.Canny(img, 125, 175)
cv.imshow("canny", canny)

contours, hierarchies

cv.waitKey(0)
