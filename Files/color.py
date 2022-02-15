import cv2
import numpy as np
from numpy import empty
import pyautogui
import imutils


def empty(a):
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def circle(img, mask):
    elements=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    for e in elements:
        ((x, y), rayon)=cv2.minEnclosingCircle(e)
        if rayon>5:
            cv2.circle(img, (int(x), int(y)), 2, (0, 0, 255), 10)
            print(x, y)

path = 'pogo/new-poke.JPG'
kernel = np.ones((5, 5), np.uint8)


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 640)
cv2.createTrackbar("Hue Min", "TrackBars", 94, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 137, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 177, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 224, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

#Pokestop
#94 137 177 255 224 255
#Pokemon
#0 21 149 255 69 255

img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
img = img[100:1799, 80:1040]
# img = imutils.resize(img, width=320, height=300)

while True:
    print("==========================")

    # fimg = cv2.imread(path)
    # img = fimg[550:850, 150:450]

    # Mask

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=3)

    imgResult = cv2.bitwise_and(img, img,mask=mask)

    # Circle

    # circle(img, mask)


    imgStack = stackImages(1, ([img, imgHSV],[mask, imgResult]))
    cv2.imshow("Stacked Images", imgStack)

    key=cv2.waitKey(1)

    if key==ord('q'):
        break
    if key==ord('s'):
        img = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        img = img[100:1799, 80:1040]