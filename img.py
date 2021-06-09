from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np
import sys

img = cv.imread("input.jpg")
cv.imshow("img", img)
color = ("b", "g", "r")
image = cv.imread("input.jpg", cv.IMREAD_COLOR)
unique_pixels = np.unique(image.reshape(-1, image.shape[2]), axis=0)
# np.set_printoptions(threshold=sys.maxsize)
print(unique_pixels)
for i, color in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.title("img")
    plt.xlabel("bins")
    plt.ylabel("amount of pixels")
    plt.plot(hist, color=color)
    plt.xlim([0, 260])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
