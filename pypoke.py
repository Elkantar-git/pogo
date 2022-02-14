import numpy as np
import cv2

ROOT_COLAB = '.'
YOLO_CONFIG = ROOT_COLAB + '/yolo_env/'
COCO_LABELS_FILE = YOLO_CONFIG + 'piford.names'
YOLO_CONFIG_FILE = YOLO_CONFIG + 'yolov4-custom.cfg'
YOLO_WEIGHTS_FILE = YOLO_CONFIG + 'yolov4-custom_best.weights'
IMAGE_FILE = 'img/Dataset/frame23.jpg'
IMAGE = cv2.imread(ROOT_COLAB + '/' + IMAGE_FILE, cv2.IMREAD_UNCHANGED)
CONFIDENCE_MIN = 0.5


# Take labels

with open(COCO_LABELS_FILE, 'rt') as f:
    labels = f.read().rstrip('\n').split('\n')


# COLORS

np.random.seed(45)
BOX_COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")


# Init network

yolo = cv2.dnn.readNetFromDarknet(YOLO_CONFIG_FILE, YOLO_WEIGHTS_FILE)

yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)

yololayers = [yolo.getLayerNames()[i - 1] for i in yolo.getUnconnectedOutLayers()]

(H, W) = IMAGE.shape[:2]

blobimage = cv2.dnn.blobFromImage(IMAGE, 1 / 255.0, (416, 416), swapRB=True, crop=False)

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


label_names = [labels[i] for i in labels_detected]
label_names


image = IMAGE.copy()
if len(boxes_detected) > 0:
  for i in range(len(boxes_detected)):
    # extract the bounding box coordinates
    (x, y) = (boxes_detected[i][0], boxes_detected[i][1])
    (w, h) = (boxes_detected[i][2], boxes_detected[i][3])
    # draw a bounding box rectangle and label on the image
    color = [int(c) for c in BOX_COLORS[labels_detected[i]]]
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    score = str(round(float(confidences_scores[i]) * 100, 1)) + "%"
    text = "{}: {}".format(labels[labels_detected[i]], score)
    cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
   

while True:
    cv2.imshow("img", image)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()