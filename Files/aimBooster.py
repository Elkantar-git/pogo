from pyautogui import *
import pyautogui
import time
import cv2
import numpy as np

time.sleep(2)



#Color of center: (255, 219, 195)

# while True:
#     flag = 0
#     pic = pyautogui.screenshot(region=(840, 800, 1200, 840))


#     width, height = pic.size
#     print(width, height)
#     for x in range(0, width, 5):
#         for y in range(0, height, 5):

#             r, g, b, w = pic.getpixel((x, y))

#             if b == 195 and r == 255 and g == 219:
#                 flag = 1
#                 print(x+840, y+800)
#                 time.sleep(0.05)
#                 break

#         if flag == 1:
#             break
while True:
        
    pic = pyautogui.screenshot(region=(840, 800, 1200, 840))
    # pic = np.array(pic)
    pic = cv2.cvtColor(np.array(pic), cv2.COLOR_BGR2RGB)
    cv2.imshow("img", pic)

    key=cv2.waitKey(1)

    if key==ord('q'):
        break