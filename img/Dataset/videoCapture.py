import cv2

count=1
vidcap = cv2.VideoCapture('file.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("frame"+str(count)+".jpg", image) # Save frame as JPG file
    return hasFrames
sec = 0
frameRate = 30 # Change this number to 1 for each 1 second

success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)