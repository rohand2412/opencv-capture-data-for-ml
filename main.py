#!/usr/bin/env python3
"""This script rapidly capture images and stores them for later labeling and usage as data"""

import cv2
import modules

img_dir = modules.DirectoryManagement(target_dir=r'/home/pi/Documents/Images/',
                                      first_dir_name="Test0")
img_dir.add()
img_dir.debug(False)

fps = modules.fps()

frame = modules.Frame(0, 300, "Cam", "img", 30)

try:
    while frame.get_cap().isOpened():
        fps.open_timer()
        frame.capture_frame()
        frame.preprocessing()
        frame.imshow()
        frame.update()
        fps.close_timer()

except modules.Break:
    frame.get_cap().release()
    cv2.destroyAllWindows()

    fps.calculate()
    fps.debug(False)
    fps.print_fps()

    frame.export_buffer()
