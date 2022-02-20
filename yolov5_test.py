import cv2
import torch
import pandas as pd
import numpy as np
from PIL import ImageGrab


# Def



# VARIABLES
CONF_MIN = 0.5


# Model
model = torch.hub.load('/Users/elkantar/projects/yolov5', 'custom', path='/Users/elkantar/projects/Pogo-Bot/pogo/best.pt', source='local')

# Image
img = ImageGrab.grab(bbox =(1024, 684, 1856, 1516))  # take a screenshot bbox=(left_x, top_y, right_x, bottom_y)
imgGREY = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

def ok():
# Inference
    results = model(imgGREY)
    results.print()
    results.show()

# Extract sorted results
    findPokemon = 0
    results = results.pandas().xyxy[0].sort_values(by=['class', 'confidence'], ascending=False).to_dict(orient="records")
    for result in results:
        # Filter labels and confidence
        if result['class'] == 1 and result['confidence'] > CONF_MIN:
            findPokemon += 1
            con = result['confidence']
            cs = result['class']
            x1 = int(result['xmin'])
            y1 = int(result['ymin'])
            x2 = int(result['xmax'])
            y2 = int(result['ymax'])
            xcenter = x1 + (x2 - x1) 
            ycenter = y1 + (y2 - y1) 
            xpos = (xcenter + 1024)/2
            ypos = (ycenter + 684)/2
            print(cs, con, x1, y1, xcenter, ycenter, xpos, ypos)

    print(f"====== Yolo find {findPokemon} Pokémon ======")

ok()


