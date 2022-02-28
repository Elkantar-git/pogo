from audioop import cross
from mimetypes import init
from PIL import ImageGrab
import cv2
import torch
import pyautogui
import PIL
import numpy as np
import pandas as pd
import time



CONF_MIN = 0.1
POKE_BUTTON = 'pogo/img/ui_pokeball_button.png'

# Init network
def initYolo():
        # Model
    model = torch.hub.load('/Users/elkantar/projects/yolov5', 'custom', path='/Users/elkantar/projects/Pogo-Bot/pogo/best.pt', source='local')
    return model


def yoloSearchPokemon(model):
    while True:
        try:
                # Image
            img = ImageGrab.grab(bbox =(1024, 624, 1856, 1456))  # take a screenshot bbox=(xmin, ymin, xmax, ymax)
            imgGREY = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
            x, y = results(imgGREY, model)
            break
        except TypeError:
            continue
    return x, y


def results(image, model):
        # Inference
    results = model(image)
    results.print()
    # results.show()

        # Extract results
    results = results.pandas().xyxy[0].sort_values(by=['class', 'confidence'], ascending=False).to_dict(orient="records")
    for result in results:
            # Filter labels and confidence
        if result['class'] == 1: # and result['confidence'] > CONF_MIN:
            # cs = result['class']
            con = result['confidence']
            x1 = int(result['xmin'])
            y1 = int(result['ymin'])
            x2 = int(result['xmax'])
            y2 = int(result['ymax'])
                # Out center
            centerX = x1 + ((x2 - x1)/2) 
            centerY = y1 + ((y2 - y1)/2)
                # Position on screen
            posX = (centerX + 1024)/2
            posY = (centerY + 624)/2
            acc = con * 100
            # print(cs, con, x1, y1, xcenter, ycenter, xpos, ypos)
            print(f'Locate position in [{posX}, {posY}] with an accuracy of : {acc} %')
            return posX, posY


def catchPokemonOrQuit(x, y):
    poke = None
    stop = None
    arena = None
    rocket = None
    rocket_battle = None
    catch = None
    onMap = None
    compteur = 0

    # Click on it
    pyautogui.click(x, y)
    # time.sleep(1)

    # Verify the page
    while poke or stop or arena or rocket or rocket_battle or onMap == None:
        poke = pyautogui.locateCenterOnScreen('pogo/locate_img/ball.jpg', grayscale=True, confidence=.8, region=(1680, 1460, 140, 140)) # , region=(1750, 1500, 150, 150)
        # Catch pokemon
        if poke != None:
            print('Catching Pokemon...')
            while pyautogui.locateCenterOnScreen('pogo/locate_img/ball.jpg', grayscale=True, confidence=.8, region=(1680, 1460, 140, 140)) != None:
                pyautogui.moveTo(725, 825)
                pyautogui.dragTo(725, 600, 0.2, button='left')
                time.sleep(1)
                while catch or onMap == None:
                    catch = pyautogui.locateCenterOnScreen('pogo/locate_img/ball.jpg', grayscale=True, confidence=.8, region=(1680, 1460, 140, 140))
                    onMap = pyautogui.locateCenterOnScreen('pogo/locate_img/menu.jpg', grayscale=True, confidence=.8) # , region=(1380, 1600, 130, 130)
                    if catch != None:
                        compteur += 1
                        print('Pokemon: NOPE... try again !')
                        catch = None
                        break
                    elif onMap != None:
                        compteur += 1
                        print(f'Pokemon {compteur} Shot Catch')
                        onMap = None
                        break
            break

        onMap = pyautogui.locateCenterOnScreen('pogo/locate_img/menu.jpg', grayscale=False, confidence=.8)
        if onMap != None:
            print('ERROR_YOLO: This is the Map')
            break

        stop = pyautogui.locateCenterOnScreen('pogo/locate_img/cross_menu.jpg', grayscale=False, confidence=.8) # , region=(1400, 1600, 100, 100)
            # Quit pokestop
        if stop != None:
            print('PokeStop Detected')
            stopxy = pyautogui.locateCenterOnScreen('pogo/locate_img/cross_menu.jpg', grayscale=False, confidence=.8)
            pyautogui.click(stopxy[0]/2, stopxy[1]/2)
            print('Quit PokeStop')
            time.sleep(1)

            # Detect TeamRocket
            rocket = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket.jpg', grayscale=False, confidence=.8, region=(960, 1500, 100, 140))
            if rocket != None:
                print('TeamRocket Detected')
                pyautogui.click(rocket[0]/2, rocket[1]/2)
                while pyautogui.locateCenterOnScreen('pogo/locate_img/rocket.jpg', grayscale=False, confidence=.8, region=(960, 1500, 100, 140)) != None:
                    pyautogui.click(rocket[0]/2, rocket[1]/2)
                    time.sleep(1)
                    if pyautogui.locateCenterOnScreen('pogo/locate_img/rocket_battle.jpg', grayscale=False, confidence=.8, region=(1240, 1370, 400, 110)) != None:
                        break
                    
                rocket_battle = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket_battle.jpg', grayscale=False, confidence=.8, region=(1240, 1370, 400, 110))
                if rocket_battle != None:
                    pyautogui.click(rocket_battle[0]/2, rocket_battle[1]/2)
                    # To modify =>
                    time.sleep(2)
                    pyautogui.click(720, 810)
                    time.sleep(10)
                    pyautogui.click(720, 810)
                    time.sleep(5)
                    pyautogui.click(720, 810)
                    time.sleep(2)
                    print('Catching Pokemon...')
                    while pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=False, confidence=.8) != None:
                        pyautogui.moveTo(725, 825)
                        pyautogui.dragTo(725, 600, 0.2, button='left')
                        while catch or onMap == None:
                            catch = pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=False, confidence=.8)
                            onMap = pyautogui.locateCenterOnScreen('pogo/locate_img/menu.jpg', grayscale=False, confidence=.8, region=(1380, 1600, 130, 130))
                            if catch != None:
                                compteur += 1
                                print('Pokemon: NOPE... try again !')
                                catch = None
                                break
                            elif onMap != None:
                                compteur += 1
                                print(f'Shadow Pokemon {compteur} Shot Catch')
                                onMap = None
                                break
            else:
                # To modify =>
                print('No TeamRocket')
                
            break

        arena = pyautogui.locateCenterOnScreen('pogo/locate_img/cross_arena.jpg', grayscale=False, confidence=.8) # , region=(1380, 1620, 150, 150)
        # Quit arena
        if arena != None:
            print('Arena Detected')
            arenaxy = pyautogui.locateCenterOnScreen('pogo/locate_img/cross_arena.jpg', grayscale=False, confidence=.8)
            pyautogui.click(arenaxy[0]/2, arenaxy[1]/2)
            print('Quit Arena')
            break

        rocket = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket.jpg', grayscale=True, confidence=.8, region=(960, 1500, 100, 140))
        if rocket != None:
            print('TeamRocket Detected')
            pyautogui.click(rocket[0]/2, rocket[1]/2)
            while pyautogui.locateCenterOnScreen('pogo/locate_img/rocket.jpg', grayscale=True, confidence=.8, region=(960, 1500, 100, 140)) != None:
                pyautogui.click(rocket[0]/2, rocket[1]/2)
                time.sleep(1)
                if pyautogui.locateCenterOnScreen('pogo/locate_img/rocket_battle.jpg', grayscale=False, confidence=.8, region=(1240, 1370, 400, 110)) != None:
                    break
            rocket_battle = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket_battle.jpg', grayscale=False, confidence=.8, region=(1240, 1370, 400, 110))
            if rocket_battle != None:
                pyautogui.click(rocket_battle[0]/2, rocket_battle[1]/2)
                # To modify =>
                time.sleep(2)
                pyautogui.click(720, 810)

                time.sleep(10)
                pyautogui.click(720, 810)
                time.sleep(10)
                pyautogui.click(720, 810)
                time.sleep(2)
                pyautogui.click(720, 810)
                time.sleep(2)
                print('Catching Pokemon...')
                while pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=False, confidence=.8) != None:
                    pyautogui.moveTo(725, 825)
                    pyautogui.dragTo(725, 600, 0.2, button='left')
                    while catch or onMap == None:
                        catch = pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=False, confidence=.8)
                        onMap = pyautogui.locateCenterOnScreen('pogo/locate_img/menu.jpg', grayscale=False, confidence=.8, region=(1380, 1600, 130, 130))
                        if catch != None:
                            compteur += 1
                            print('Pokemon: NOPE... try again !')
                            catch = None
                            break
                        elif onMap != None:
                            compteur += 1
                            print(f'Shadow Pokemon {compteur} Shot Catch')
                            onMap = None
                            break
                break
            else:
                # To modify =>
                pyautogui.click(720, 840)
                print('Quit Rocket')
                break

        # rocket_battle = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket_battle.jpg', grayscale=True, confidence=.8)
        rocket_battle = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket_battle.jpg', grayscale=False, confidence=.8, region=(1240, 1370, 400, 110))
        if rocket_battle != None:
            pyautogui.click(rocket_battle[0]/2, rocket_battle[1]/2)
            # To modify =>
            time.sleep(2)
            pyautogui.click(720, 810)
            time.sleep(10)
            pyautogui.click(720, 810)
            time.sleep(5)
            pyautogui.click(720, 810)
            time.sleep(2)
            print('Catching Pokemon...')
            while pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=False, confidence=.8) != None:
                pyautogui.moveTo(725, 825)
                pyautogui.dragTo(725, 600, 0.2, button='left')
                while catch or onMap == None:
                    catch = pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=False, confidence=.8)
                    onMap = pyautogui.locateCenterOnScreen('pogo/locate_img/menu.jpg', grayscale=False, confidence=.8, region=(1380, 1600, 130, 130))
                    if catch != None:
                        compteur += 1
                        print('Pokemon: NOPE... try again !')
                        catch = None
                        break
                    elif onMap != None:
                        compteur += 1
                        print(f'Shadow Pokemon {compteur} Shot Catch')
                        onMap = None
                        break
            break
        # else:
        #     # To modify =>
        #     pyautogui.click(720, 840)
        #     print('Quit Rocket')
        #     break

    # MAIN

model = initYolo()

while True:
    print('============SEARCHING POKEMON...============')

    x, y = yoloSearchPokemon(model)

    catchPokemonOrQuit(x, y)

    


    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
