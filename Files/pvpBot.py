# PvpBot



# BATTLE SCEEN

# Start at the battle sceen

# Click on BATTLE
# Click choose League
# Click Go


# FIGHT

# Spam first attack
# Click on the charged attack
# Complete the disign
# 
# 
# If pink pixel apeard => Shield
# 


# Screenshot
# Spam first, charged attack and shield on [290:800]

# Detect the color of the charged attack and lookAt()
    # 
# Click on the Design in 5s
# Spam





# NEXT FIGHT OR REWARDS

# Click on Next
# Click on League
# Click Go

# For rewards Click on Orange pixel



import cv2
import numpy as np
import pyautogui
from pyautogui import *
import imutils



def lookAt(forWhat):                    # x, y = Full sceen
    if forWhat == "Battle":
        return 720, 1700, 1, 1
    elif forWhat == "pix":
        return 572, 1542, 1, 1
    elif forWhat == "atkDragon":
        return 100, 400, 300, 1040
    elif forWhat == "atkEau":
        return xmin, xmax, ymin, ymax
    elif forWhat == "atkFeu":
        return xmin, xmax, ymin, ymax
    elif forWhat == "atk":
        return xmin, xmax, ymin, ymax


# def screenshot(xmin, xmax, ymin, ymax):
#     img = pyautogui.screenshot(region=(xmin, xmax, ymin, ymax))

#     width, height = img.size()
#     # img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#     # img = np.array(img)
#     # img = img[ymin:ymax, xmin:xmax]            
#     # img = imutils.resize(img, width=(xmax-xmin)/2, height=(ymax-ymin)/2) 
#     return img


# BATTLE SCEEN

xmin, xmax, ymin, ymax = lookAt("Battle")


img = pyautogui.screenshot(region=(xmin, xmax, ymin, ymax))

width, height = img.size
# print(width, height)

for x in range(0, width, 5):
    for y in range(0, height, 5):
        r, g, b, w = img.getpixel((x, y))
        # print(r, g, b, w)
        if g == 208:
            pyautogui.click(xmin/2, xmax/2)
            time.sleep(0.5)
            pyautogui.click(xmin/2, xmax/2)
            time.sleep(5)
            pyautogui.click(400, 400)
            time.sleep(5)
            pyautogui.click(430, 800)

# Green battle (67, 208, 164, 255)




#  BATTLE

while True:

    # px= pyautogui.pixel(572,1542)
    # print(px)
    # if pyautogui.pixel(572,1542)[0] > 220 and pyautogui.pixel(572,1542)[1] > 220 and pyautogui.pixel(572,1542)[2] > 220: 
        # xmin, xmax, ymin, ymax = lookAt("atkDragon")
        img = pyautogui.screenshot(region=(100, 400, 300, 1040))
        width, height = img.size
        # print(width, height)

        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r, g, b, w = img.getpixel((x, y))
                # print(r, g, b)
                if ((r in range(3, 9)) and (g in range(125, 131)) and (b in range(187, 193))):
                # if r == 6 and g == 128 and b == 190:
                    pyautogui.moveTo(x+50, y+200)
                    print(x, y)
                    # time.sleep(0.05)
                    break
