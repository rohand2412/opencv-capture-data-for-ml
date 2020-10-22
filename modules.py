import os
import numpy as np
import datetime
import cv2

class DirectoryManagement:
    def __init__(self, targetDir):
        self._targetDir = targetDir
        os.chdir(targetDir)
    
    def getTargetDir(self):
        return self._targetDir

    def setFirstDirName(self, firstDirName):
        self._firstDirName = firstDirName
    
    def getFirstDirName(self):
        return self._firstDirName
    
    def add(self):
        self._names = os.listdir(self.getTargetDir())
        self._nums = []
        self._mostRecentDir = self._MostRecentDir()
        self._newFolder = None
        if self._names:
            self._names = np.sort(self._names)
            self._nums = []
            for name in self._names:
                self._nums = np.append(self._nums, int(''.join(filter(str.isdigit, name))))
            self._mostRecentDir.calculate(self._names, self._nums)
            self._newFolder = self._mostRecentDir.getText() + str(self._mostRecentDir.getNum()+1)
        else:
            self._newFolder = self.getFirstDirName()
        os.mkdir(self._newFolder)
        os.chdir(self._newFolder)

    def debug(self, debug):
        if debug:
            print("names: " + str(self._names))
            print("nums: " + str(self._nums))
            self._mostRecentDir.debug(True)
            print("newFolder: " + str(self._newFolder))
    
    class _MostRecentDir:
        def __init__(self):
            self._index = None
            self._name = None
            self._num = None
            self._text = None
        
        def calculate(self, names, nums):
            self._num = np.amax(nums)
            self._index = int(np.where(nums == self._num)[0])
            self._name = names[self._index]
            self._num = int(''.join(filter(str.isdigit, self._name)))
            self._text = ''.join(filter(str.isalpha, self._name))
        
        def getIndex(self):
            return self._index
        
        def getName(self):
            return self._name
        
        def getNum(self):
            return self._num
        
        def getText(self):
            return self. _text
        
        def debug(self, debug):
            if debug:
                print("MostRecentDir: index: " + str(self._index))
                print("MostRecentDir: name: " + str(self._name))
                print("MostRecentDir: num: " + str(self._num))
                print("MostRecentDir: text: " + str(self._text))

class FPS:
    def __init__(self):
        self._elapsedTimes = np.array([])
        self._MS_TO_SECONDS = 1.0/1000000.0
    
    def openTimer(self):
        self._startTime = datetime.datetime.now()
    
    def closeTimer(self):
        self._endTime = datetime.datetime.now()
        self._elapsedTimes = np.append(self._elapsedTimes, self._endTime - self._startTime)
        return self._elapsedTimes[-1]
    
    def calculate(self):
        self._elapsedTimes = np.delete(self._elapsedTimes, [0])
        self._mean = np.mean(self._elapsedTimes)
        self._secondsPerFrame = self._mean.microseconds * self._MS_TO_SECONDS
        self._fps = 1.0/self._secondsPerFrame
    
    def getFPS(self):
        return self._fps

    def printFPS(self):
        print("FPS: " + str(self._fps))
    
    def debug(self, debug):
        if debug:
            print("startTime: " + str(self._startTime))
            print("endTime: " + str(self._endTime))
            print("elapsedTimes: " + str(self._elapsedTimes))
            print("mean: " + str(self._mean))
            print("secondsPerFrame: " + str(self._secondsPerFrame))
            print("fps: " + str(self._fps))

class Frame:
    def __init__(self, side, name, filename, limitOfFrames=None):
        self._name = name
        self._filename = filename
        self._cap = cv2.VideoCapture(0)
        self._width = self._cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self._height = self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self._side = side
        self._limitOfFrames = limitOfFrames
        self._frameNum = 1
        self._frameBuffer = np.array([])
    
    def captureFrame(self):
        self._ret, self._frame = self._cap.read()
    
    def preprocessing(self):
        self._frame = cv2.flip(self._frame, 1)
        self._frame = self._frame[int((self._height-self._side)/2):
                                  int((self._height+self._side)/2), 
                                  int((self._width-self._side)/2):
                                  int((self._width+self._side)/2)]
        self._frameBuffer = np.append(self._frameBuffer, self._frame)
    
    def imshow(self):
        cv2.imshow(self._name, self._frame)
    
    def update(self):
        if self._limitOfFrames:
            if self._frameNum >= self._limitOfFrames:
                break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        self._frameNum += 1
    
    def exportBuffer(self):
        for frame in self._frameBuffer:
            index = int(np.where(self._frameBuffer == frame)[0][0])
            cv2.imwrite(self._filename + str(index+1) + ".jpg", frame)