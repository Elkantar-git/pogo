import numpy as np
import cv2
import pyautogui
import time


    # PAGES

def locateOnScreen(x):
    if x == 'menu':
        menu = pyautogui.locateCenterOnScreen('pogo/locate_img/items/menu.jpg', grayscale=True, confidence=.8, region=(1380, 1600, 130, 130))
        return menu[0], menu[1]
        # print(menu)

    if x == 'cross':
        cross = pyautogui.locateCenterOnScreen('pogo/locate_img/items/cross_menu.jpg', grayscale=True, confidence=.8, region=(1400, 1600, 100, 100))
        print(cross)

    if x == 'poke':
        poke = pyautogui.locateCenterOnScreen('pogo/locate_img/items/poke_menu.jpg', grayscale=True, confidence=.8, region=(1100, 1450, 150, 130))
        # print(poke)

    if x == 'item':
        item = pyautogui.locateCenterOnScreen('pogo/locate_img/items/item_menu.jpg', grayscale=True, confidence=.8, region=(1650, 1450, 120, 120))
        # print(item)

    if x == 'crossPage':
        crossPage = pyautogui.locateCenterOnScreen('pogo/locate_img/items/cross_page.jpg', grayscale=True, confidence=.8, region=(1390, 1620, 110, 110))
        # print(crossPage)

    # if x == 'menu':
        # rocketBattle = pyautogui.locateCenterOnScreen('pogo/rocket_battle.jpg', grayscale=True, confidence=.8, region=(1340, 1380, 200, 90))
        # print(rocketBattle)


    # CLEAR ITEMS

def delete_item(xItem):
    if xItem != None:
        pyautogui.click(xItem[0]/2 + 347, xItem[1]/2)
        time.sleep(2)
        pyautogui.click(600, 420)
        time.sleep(2)
        pyautogui.click(700, 575)
        time.sleep(2)


def clear_items():
    pItem = pyautogui.locateCenterOnScreen('pogo/locate_img/items/p_item.jpg', grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
    print('Potion', pItem)
    delete_item(pItem)

    spItem = pyautogui.locateCenterOnScreen('pogo/locate_img/items/sp_item.jpg', grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
    print('Super Potion', spItem)
    delete_item(spItem)

    hpItem = pyautogui.locateCenterOnScreen('pogo/locate_img/items/hp_item.jpg', grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
    print('Hyper Potion', hpItem)
    delete_item(hpItem)

    rItem = pyautogui.locateCenterOnScreen('pogo/locate_img/items/r_item.jpg', grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
    print('Revive', rItem)
    delete_item(rItem)

    while True:
        pyautogui.moveTo(850, 850)
        pyautogui.dragTo(850, 170, 2.5, button='left')
        time.sleep(1.5)

        rbItem = pyautogui.locateCenterOnScreen('pogo/locate_img/items/rb_item.jpg', grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
        print('Razz Berry', rbItem)
        delete_item(rbItem)

        nbItem = pyautogui.locateCenterOnScreen('pogo/locate_img/items/nb_item.jpg', grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
        print('Nanab Berry', nbItem)
        delete_item(nbItem)

        pbItem = pyautogui.locateCenterOnScreen('pogo/locate_img/items/pb_item.jpg', grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
        print('Pinap Berry', pbItem)
        delete_item(pbItem)

        iItem = pyautogui.locateCenterOnScreen('pogo/locate_img/items/i_item.jpg', grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
        print('Incub Inf.', iItem)

        if iItem != None:
            break




clear_items()



# locateOnScreen('cross')














