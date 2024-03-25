import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)


blank[200:300, 300:400] = 0, 0, 255


cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.imshow("rectangle", blank)

cv.waitKey(0)
