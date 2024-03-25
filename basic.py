import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow("Cat", img)


# conver to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# dilate
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)
# erode
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Crop
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)
cv.waitKey(0)
