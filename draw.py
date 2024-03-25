import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)


blank[200:300, 300:400] = 0, 0, 255


cv.rectangle(
    blank,
    (0, 0),
    (blank.shape[1] // 2, blank.shape[1] // 2),
    (0, 255, 0),
    thickness=cv.FILLED,
)
cv.imshow("rectangle", blank)

cv.circle(
    blank, (blank.shape[1] // 2, blank.shape[1] // 2), 40, (0, 0, 255), thickness=3
)
cv.imshow("circle", blank)

cv.line(
    blank,
    (100, 250),
    (blank.shape[1] // 2, blank.shape[1] // 2),
    (255, 255, 255),
    thickness=3,
)
cv.imshow("line", blank)

cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv.imshow("text", blank)
cv.waitKey(0)
