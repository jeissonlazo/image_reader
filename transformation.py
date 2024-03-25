import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")

cv.imshow("Bostron", img)


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)


translated = translate(img, -100, 100)
cv.imshow("Translated", translated)


# Rotation


def rotation(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPont = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotation(img, 45)
cv.imshow("Rotated", rotated)

rotate_rotate = rotation(rotated, -45)
cv.imshow("Rotatex2", rotate_rotate)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resize", resized)

# Flip

flip = cv.flip(img, -1)
cv.imshow("flip", flip)

# Crop
crop = img[200:400, 300:400]
cv.imshow("crop", crop)
cv.waitKey(0)
