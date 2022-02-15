from multiprocessing.connection import wait
import pyautogui
import time


# time.sleep(2)
# a = pyautogui.size()
# print(a)

def Spin():
    pyautogui.moveTo(300, 450)
    pyautogui.dragTo(80, 450, 0.2, button='left')
    time.sleep(0.5)
    pyautogui.click(x=280, y=840)

if __name__ == '__main__':

    Spin()