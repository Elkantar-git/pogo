import numpy as np
import cv2
import pyautogui
import time
import PIL

LABELS_FILE = 'pogo/yolo_env/piford.names'
CONFIG_FILE = 'pogo/yolo_env/yolov4-custom.cfg'
WEIGHTS_FILE = 'pogo/yolo_env/yolov4-custom_best.weights'
CONFIDENCE_MIN = 0.8
POKE_BUTTON = 'pogo/img/ui_pokeball_button.png'

# Init network

yolo = cv2.dnn.readNetFromDarknet(CONFIG_FILE, WEIGHTS_FILE)

yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

yololayers = [yolo.getLayerNames()[i - 1] for i in yolo.getUnconnectedOutLayers()]


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
                print(boxes_detected)
                print(confidences_scores)

                return centerX, centerY

def catchPokemon():

    time.sleep(5)
    while pyautogui.pixelMatchesColor(1800, 1580, (215, 48, 27), tolerance=50) == True:
        pyautogui.moveTo(725, 825)
        pyautogui.dragTo(725, 600, 0.2, button='left')
        time.sleep(5)
        print('ok')
    # img = pyautogui.screenshot(region=(1800, 1580, 1, 1))
    # px = img.getpixel((0, 0))
    # p = pyautogui.pixelMatchesColor(1800, 1580, (215, 48, 27), tolerance=10)
    # print(px)
    # print(p)


# 900, 790

while True:
    print('============START============')


    # cv2.imshow("img", image)

    while True:
        try:
            img = pyautogui.screenshot(region=(964, 800, 950, 750))  # Full Screen = 964, 170, 950, 1628
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            x, y = yoloxy(image, yolo, yololayers)
            break
        except:
            continue

        
    print(x, y)

    pyautogui.moveTo(x/2 + 482, y/2 + 400)
    pyautogui.click()

    catchPokemon()


    


    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
