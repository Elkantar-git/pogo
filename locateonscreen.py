import numpy as np
import cv2
import pyautogui
import time


    # PAGES

def locateOnScreen(x):
    if x == 'menu':
        menu_menu = 'pogo/menu.jpg'
        menu = pyautogui.locateCenterOnScreen(menu_menu, grayscale=True, confidence=.8, region=(1380, 1600, 130, 130))
        return menu[0], menu[1]
        # print(menu)

    if x == 'cross':
        cross_menu_stop = 'pogo/cross_menu.jpg'
        cross = pyautogui.locateCenterOnScreen(cross_menu_stop, grayscale=True, confidence=.8, region=(1400, 1600, 100, 100))
        print(cross)

    if x == 'poke':
        poke_menu = 'pogo/poke_menu.jpg'
        poke = pyautogui.locateCenterOnScreen(poke_menu, grayscale=True, confidence=.8, region=(1100, 1450, 150, 130))
        # print(poke)

    if x == 'item':
        item_menu = 'pogo/item_menu.jpg'
        item = pyautogui.locateCenterOnScreen(item_menu, grayscale=True, confidence=.8, region=(1650, 1450, 120, 120))
        # print(item)

    if x == 'crossPage':
        cross_page = 'pogo/cross_page.jpg'
        crossPage = pyautogui.locateCenterOnScreen(cross_page, grayscale=True, confidence=.8, region=(1390, 1620, 110, 110))
        # print(crossPage)

    # if x == 'menu':
        # rocket_battle = 'pogo/rocket_battle.jpg'
        # rocketBattle = pyautogui.locateCenterOnScreen(rocket_battle, grayscale=True, confidence=.8, region=(1340, 1380, 200, 90))
        # print(rocketBattle)


# CLEAR ITEMS

def clear_items():
    p_item = 'pogo/p_item.jpg'
    pItem = pyautogui.locateCenterOnScreen(p_item, grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
    print('Potion', pItem)

    if pItem != None:
        pyautogui.click(pItem[0]/2 + 347, pItem[1]/2)
        time.sleep(2)
        pyautogui.click(600, 420)
        time.sleep(2)
        pyautogui.click(700, 575)
        time.sleep(2)

    sp_item = 'pogo/sp_item.jpg'
    spItem = pyautogui.locateCenterOnScreen(sp_item, grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
    print('Super Potion', spItem)

    if spItem != None:
        pyautogui.click(spItem[0]/2 + 347, spItem[1]/2)
        time.sleep(2)
        pyautogui.click(600, 420)
        time.sleep(2)
        pyautogui.click(700, 575)
        time.sleep(2)

    hp_item = 'pogo/hp_item.jpg'
    hpItem = pyautogui.locateCenterOnScreen(hp_item, grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
    print('Hyper Potion', hpItem)

    if hpItem != None:
        pyautogui.click(hpItem[0]/2 + 347, hpItem[1]/2)
        time.sleep(2)
        pyautogui.click(600, 420)
        time.sleep(2)
        pyautogui.click(700, 575)
        time.sleep(2)

    r_item = 'pogo/r_item.jpg'
    rItem = pyautogui.locateCenterOnScreen(r_item, grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
    print('Revive', rItem)

    if rItem != None:
        pyautogui.click(rItem[0]/2 + 347, rItem[1]/2)
        time.sleep(2)
        pyautogui.click(600, 420)
        time.sleep(2)
        pyautogui.click(700, 575)
        time.sleep(2)


    while True:

        pyautogui.moveTo(850, 850)
        pyautogui.dragTo(850, 170, 2.5, button='left')
        time.sleep(1.5)


        rb_item = 'pogo/rb_item.jpg'
        rbItem = pyautogui.locateCenterOnScreen(rb_item, grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
        print('Razz Berry', rbItem)

        if rbItem != None:
            pyautogui.click(rbItem[0]/2 + 347, rbItem[1]/2)
            time.sleep(2)
            pyautogui.click(600, 420)
            time.sleep(2)
            pyautogui.click(700, 575)
            time.sleep(2)

        nb_item = 'pogo/nb_item.jpg'
        nbItem = pyautogui.locateCenterOnScreen(nb_item, grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
        print('Nanab Berry', nbItem)

        if nbItem != None:
            pyautogui.click(nbItem[0]/2 + 347, nbItem[1]/2)
            time.sleep(2)
            pyautogui.click(600, 420)
            time.sleep(2)
            pyautogui.click(700, 575)
            time.sleep(2)

        pb_item = 'pogo/pb_item.jpg'
        pbItem = pyautogui.locateCenterOnScreen(pb_item, grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
        print('Pinap Berry', pbItem)

        if pbItem != None:
            pyautogui.click(pbItem[0]/2 + 347, pbItem[1]/2)
            time.sleep(2)
            pyautogui.click(600, 420)
            time.sleep(2)
            pyautogui.click(700, 575)
            time.sleep(2)

        i_item = 'pogo/i_item.jpg'
        iItem = pyautogui.locateCenterOnScreen(i_item, grayscale=False, confidence=.8, region=(1000, 330, 270, 1468))
        print('Incub Inf.', iItem)

        if iItem != None:
            break




clear_items()



locateOnScreen('cross')














