
import cv2
import numpy as np
import imutils

img = cv2.imread(cv2.samples.findFile("base.png"))

resized = imutils.resize(img, width=300)
ratio = img.shape[0] / float(resized.shape[0])

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
thres = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY)[1]

roi = thres[200:400, 100:200]


cv2.imshow("Display window", roi)

k = cv2.waitKey(0)

