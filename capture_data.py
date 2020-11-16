#!/usr/bin/env python3
"""This script rapidly capture images and stores them for later labeling and usage as data"""

import cv2
from capture_data_utils import CaptureData

def main():
    """Main code"""
    img_dir = CaptureData.DirectoryManagement.WriteDir(target_dir=r'/home/pi/Documents/Images/',
                                                   first_dir_name="Test0")
    img_dir.add()
    img_dir.debug(False)

    fps = CaptureData.Fps()

    frame = CaptureData.Frame(side=300, name="Cam", filename="img", limit_of_frames=180)

    try:
        while True:
            fps.open_timer()
            frame.capture_frame()
            frame.preprocessing()
            frame.imshow()
            frame.update()

            CaptureData.check_for_quit_request()

            print(fps.close_timer())

    except CaptureData.Break:
        frame.get_camera().stop()
        cv2.destroyAllWindows()

        fps.calculate()
        fps.debug(False)
        fps.print_fps()

        frame.export_buffer()

if __name__ == '__main__':
    main()
