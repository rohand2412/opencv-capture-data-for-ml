import cv2
import datetime
import numpy as np
import os
import modules

cap = cv2.VideoCapture(0)

imgs = modules.DirectoryManagement(r'/home/pi/Documents/Images/')
imgs.setFirstDirName("Test0")
imgs.add()
imgs.debug(True)

while(True):
    pass

limitOfImgs = 30
elapsed_times = np.array([])
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
side = 300
frameNum = 1

while(cap.isOpened()):
    start_time = datetime.datetime.now()
    
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame = frame[int((height-side)/2):int((height+side)/2), int((width-side)/2):int((width+side)/2)]

    cv2.imshow('frame', frame)
    cv2.imwrite("img" + str(frameNum) + ".jpg", frame)

    if frameNum >= limitOfImgs:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    end_time = datetime.datetime.now()
    elapsed_times = np.append(elapsed_times, end_time - start_time)
    print(elapsed_times[frameNum-1])

    frameNum += 1

print("FPS: " + str(1.0/(np.mean(np.delete(elapsed_times, [0]))).seconds))

cap.release()
cv2.destroyAllWindows()