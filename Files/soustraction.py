
import cv2
import numpy as np
import imutils


def calcul_mask(img, fond, seuil):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img.shape
    mask = np.zeros([height, width], np.uint8)
    img = img.astype(np.int32)
    for y in range(height):
        for x in range(width):
            if abs(fond[y][x] - img[y][x]) > seuil:
                mask[y][x] = 255
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=3)

    return mask


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




seuil = 50

xmin = 150
xmax = 450
ymin = 550
ymax = 850


img_fond = cv2.imread("pogo/new.JPG")
img_fond = cv2.cvtColor(img_fond, cv2.COLOR_BGR2GRAY)
img_fond = img_fond[ymin:ymax, xmin:xmax]

img = cv2.imread("pogo/new-poke.JPG")
img = img[ymin:ymax, xmin:xmax]

while True:
    print(seuil)
    mask = calcul_mask(img, img_fond, seuil)

    imgResult = cv2.bitwise_and(img, img,mask=mask)

    #cv2.imshow("img", img)
    #cv2.imshow("fond", img_fond)
    #cv2.imshow("mask", mask)

    imgStack = stackImages(1.2, ([img, img_fond],[mask, imgResult]))
    cv2.imshow("Stacked Images", imgStack)

    key=cv2.waitKey(1)

    if key==ord('q'):
        break
    if key==ord('p'):
        seuil+=1
    if key==ord('m'):
        seuil-=1






#resized = imutils.resize(img, width=300)
#ratio = img.shape[0] / float(resized.shape[0])

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blurred = cv2.GaussianBlur(resized, (5, 5), 0)
#thres = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY)[1]

#roi = thres[200:400, 100:200]


#cv2.imshow("Display window", roi)

#k = cv2.waitKey(0)

