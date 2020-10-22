import cv2
import modules

imgDir = modules.DirectoryManagement(r'/home/pi/Documents/Images/')
imgDir.setFirstDirName("Test0")
imgDir.add()
imgDir.debug(False)

fps = modules.FPS()

frame = modules.Frame(0, 300, "Cam", "img", 30)

try:
    while(frame.getCap().isOpened()):
        fps.openTimer()
        
        frame.captureFrame()
        frame.preprocessing()
        frame.imshow()
        frame.update()
        
        fps.closeTimer()

except modules.Break:
    frame.getCap().release()
    cv2.destroyAllWindows()

    fps.calculate()
    fps.debug(False)
    fps.printFPS()

    frame.exportBuffer()