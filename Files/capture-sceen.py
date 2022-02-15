import cv2
import numpy as np
import os
import pyautogui

# output = "video.avi"
img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#get info from img
height, width, channels = img.shape
print(height, width, channels)

while True:

  img = pyautogui.screenshot()
  image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)



  cv2.imshow("img", image)


  key=cv2.waitKey(1)
  if key==ord('q'):
      break
