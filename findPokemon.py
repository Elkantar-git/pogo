import numpy as np
import cv2
# from google.colab.patches import cv2_imshow

ROOT_COLAB = '.'
YOLO_CONFIG = ROOT_COLAB + '/yolo_env/'
COCO_LABELS_FILE = YOLO_CONFIG + 'piford.names'
YOLO_CONFIG_FILE = YOLO_CONFIG + 'yolov4-custom.cfg'
YOLO_WEIGHTS_FILE = YOLO_CONFIG + 'yolov4-custom_best.weights'
IMAGE_FILE = 'img/Dataset/frame21.jpg'
# IMAGE = cv2.imread(ROOT_COLAB + '/' + IMAGE_FILE)
IMAGE = cv2.imread(ROOT_COLAB + '/' + IMAGE_FILE, cv2.IMREAD_UNCHANGED)
CONFIDENCE_MIN = 0.5

# Little function to resize in keeping the format ratio
# Cf. https://stackoverflow.com/questions/35180764/opencv-python-image-too-big-to-display
def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    image = image.copy()
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    return cv2.resize(image, dim, interpolation=inter)
 
# cv2.imshow(ResizeWithAspectRatio(IMAGE, width=700)) 




 
# img = cv2.imread('/home/img/python.png', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',IMAGE.shape)
 
scale_percent = 50 # percent of original size
width = int(IMAGE.shape[1] * scale_percent / 100)
height = int(IMAGE.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(IMAGE, dim, interpolation = cv2.INTER_AREA)
 
# print('Resized Dimensions : ',resized.shape)
 

# while True:
#     cv2.imshow("Resized image", resized)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


IMAGE = cv2.resize(IMAGE, dim, interpolation = cv2.INTER_AREA)



with open(COCO_LABELS_FILE, 'rt') as f:
    labels = f.read().rstrip('\n').split('\n')


np.random.seed(45)
BOX_COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")


yolo = cv2.dnn.readNetFromDarknet(YOLO_CONFIG_FILE, YOLO_WEIGHTS_FILE)

yololayers = [yolo.getLayerNames()[i[0] - 1] for i in yolo.getUnconnectedOutLayers()]

blobimage = cv2.dnn.blobFromImage(IMAGE, 1 / 255.0, (416, 416), swapRB=True, crop=False)
yolo.setInput(blobimage)

layerOutputs = yolo.forward(yololayers)


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
  for i in range(boxes_detected):
    # extract the bounding box coordinates
    (x, y) = (boxes_detected[i][0], boxes_detected[i][1])
    (w, h) = (boxes_detected[i][2], boxes_detected[i][3])
    # draw a bounding box rectangle and label on the image
    color = [int(c) for c in BOX_COLORS[labels_detected[i]]]
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    score = str(round(float(confidences_scores[i]) * 100, 1)) + "%"
    text = "{}: {}".format(labels[labels_detected[i]], score)
    cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
   
cv2.imshow(ResizeWithAspectRatio(image, width=700))