import cv2
import datetime
import numpy as np
import os
import modules

cap = cv2.VideoCapture(0)

imgDir = modules.DirectoryManagement(r'/home/pi/Documents/Images/')
imgDir.setFirstDirName("Test0")
imgDir.add()
imgDir.debug(False)

fps = modules.FPS()

limitOfImgs = 30
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
side = 300
frameNum = 1

while(cap.isOpened()):
    fps.openTimer()
    
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame = frame[int((height-side)/2):int((height+side)/2), int((width-side)/2):int((width+side)/2)]

    cv2.imshow('frame', frame)
    cv2.imwrite("img" + str(frameNum) + ".jpg", frame)

    if frameNum >= limitOfImgs:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    fps.closeTimer()

    frameNum += 1

fps.calculate()
fps.debug(False)
fps.printFPS()

cap.release()
cv2.destroyAllWindows()