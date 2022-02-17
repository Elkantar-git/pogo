from audioop import cross
from mimetypes import init
import numpy as np
import cv2
import pyautogui
import time
import PIL

LABELS_FILE = 'pogo/yolo_env/piford.names'
CONFIG_FILE = 'pogo/yolo_env/yolov4-custom.cfg'
WEIGHTS_FILE = 'pogo/yolo_env/yolov4-custom_best.weights'
CONFIDENCE_MIN = 0.2
POKE_BUTTON = 'pogo/img/ui_pokeball_button.png'

# Init network
def initYolo():
    yolo = cv2.dnn.readNetFromDarknet(CONFIG_FILE, WEIGHTS_FILE)
    yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    yololayers = [yolo.getLayerNames()[i - 1] for i in yolo.getUnconnectedOutLayers()]
    return yolo, yololayers


def yoloxy(image, yolo, yololayers):
    (H, W) = image.shape[:2]
    blobimage = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    yolo.setInput(blobimage)
    layerOutputs = yolo.forward(yololayers)

    # Postprocessing
    boxes_detected = []
    confidences_scores = []
    labels_detected = []
    # loop over each of the layer outputs
    for output in layerOutputs:
    # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of the current object detection
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
        
            # Take only predictions with confidence more than CONFIDENCE_MIN thresold
            if confidence > CONFIDENCE_MIN:
                # Bounding box
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")
            
                # Use the center (x, y)-coordinates to derive the top and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
            
                # update our result list (detection)
                boxes_detected.append([x, y, int(width), int(height)])
                confidences_scores.append(float(confidence))
                labels_detected.append(classID)
                # print(boxes_detected)
                # accuracy = sorted(confidences_scores)
                # print(confidences_scores)
                # print(accuracy)
                print(f'Locate position in [{centerX}, {centerY}] with an accuracy of : {confidence} %')

                return centerX, centerY


def yoloSearchPokemon(yolo, yololayers):
    while True:
        try:
            img = pyautogui.screenshot(region=(964, 800, 950, 750))  # Full Screen = 964, 170, 950, 1628
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            x, y = yoloxy(image, yolo, yololayers)
            break
        except TypeError:
            continue
    return x, y


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
    pyautogui.click(x/2 + 482, y/2 + 400)
    time.sleep(2)

    # Verify the page
    while poke or stop or arena or rocket or rocket_battle or onMap == None:
        poke = pyautogui.locateCenterOnScreen('pogo/locate_img/ball.jpg', grayscale=True, confidence=.8)
        # Catch pokemon
        if poke != None:
            print('Catching Pokemon...')
            while pyautogui.locateCenterOnScreen('pogo/locate_img/ball.jpg', grayscale=True, confidence=.8) != None:
                pyautogui.moveTo(725, 825)
                pyautogui.dragTo(725, 600, 0.2, button='left')
                while catch or onMap == None:
                    catch = pyautogui.locateCenterOnScreen('pogo/locate_img/ball.jpg', grayscale=True, confidence=.8)
                    onMap = pyautogui.locateCenterOnScreen('pogo/locate_img/menu.jpg', grayscale=True, confidence=.8, region=(1380, 1600, 130, 130))
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

        onMap = pyautogui.locateCenterOnScreen('pogo/locate_img/menu.jpg', grayscale=True, confidence=.8, region=(1380, 1600, 130, 130))
        if onMap != None:
            print('ERROR_YOLO: This is the Map')
            break

        stop = pyautogui.locateCenterOnScreen('pogo/locate_img/cross_menu.jpg', grayscale=True, confidence=.8, region=(1400, 1600, 100, 100))
            # Quit pokestop
        if stop != None:
            print('PokeStop Detected')
            stopxy = pyautogui.locateCenterOnScreen('pogo/locate_img/cross_menu.jpg', grayscale=True, confidence=.8, region=(1400, 1600, 100, 100))
            pyautogui.click(stopxy[0]/2, stopxy[1]/2)
            print('Quit PokeStop')

            # Detect TeamRocket
            rocket = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket.jpg', grayscale=True, confidence=.8, region=(960, 1500, 100, 140))
            if rocket != None:
                print('TeamRocket Detected')
                pyautogui.click(rocket[0]/2, rocket[1]/2)
                while pyautogui.locateCenterOnScreen('pogo/locate_img/rocket.jpg', grayscale=True, confidence=.8, region=(960, 1500, 100, 140)) != None:
                    pyautogui.click(rocket[0]/2, rocket[1]/2)
                    time.sleep(1)
                rocket_battle = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket_battle.jpg', grayscale=True, confidence=.8)
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
                    while pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=True, confidence=.8) != None:
                        pyautogui.moveTo(725, 825)
                        pyautogui.dragTo(725, 600, 0.2, button='left')
                        while catch or onMap == None:
                            catch = pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=True, confidence=.8)
                            onMap = pyautogui.locateCenterOnScreen('pogo/locate_img/menu.jpg', grayscale=True, confidence=.8, region=(1380, 1600, 130, 130))
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

        arena = pyautogui.locateCenterOnScreen('pogo/locate_img/cross_arena.jpg', grayscale=True, confidence=.8)
        # Quit arena
        if arena != None:
            print('Arena Detected')
            arenaxy = pyautogui.locateCenterOnScreen('pogo/locate_img/cross_arena.jpg', grayscale=True, confidence=.8)
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
            rocket_battle = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket_battle.jpg', grayscale=True, confidence=.8)
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
                while pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=True, confidence=.8) != None:
                    pyautogui.moveTo(725, 825)
                    pyautogui.dragTo(725, 600, 0.2, button='left')
                    while catch or onMap == None:
                        catch = pyautogui.locateCenterOnScreen('pogo/locate_img/berry.jpg', grayscale=True, confidence=.8)
                        onMap = pyautogui.locateCenterOnScreen('pogo/locate_img/menu.jpg', grayscale=True, confidence=.8, region=(1380, 1600, 130, 130))
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

        rocket_battle = pyautogui.locateCenterOnScreen('pogo/locate_img/rocket_battle.jpg', grayscale=True, confidence=.8)


    # # Quit rocket
    # elif rocket == True:
    #     print('Quit Rocket')

    # # Quit rocket battle
    # elif rocket_battle == True:
    #     print('Quit Rocket')
    



# 900, 790




    # MAIN

yolo, yololayers = initYolo()

while True:
    print('============SEARCHING POKEMON...============')

    x, y = yoloSearchPokemon(yolo, yololayers)

    catchPokemonOrQuit(x, y)


    


    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
