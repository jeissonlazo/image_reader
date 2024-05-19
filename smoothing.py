import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Bostron", img)

# Averaging
avarage = cv.blur(img, (7, 7))
cv.imshow("Avarage", avarage)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussian", gaussian)

# median Blur
median = cv.medianBlur(img, 7)
cv.imshow("Median", median)
# Bilateral Blur
bilateral = cv.bilateralFilter(img, 15, 35, 25)
cv.imshow("Bilateral", bilateral)
cv.waitKey(0)
