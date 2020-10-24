#!/usr/bin/env python3
"""This script rapidly capture images and stores them for later labeling and usage as data"""

import cv2
import modules

def main():
    """Main code"""
    img_dir = modules.DirectoryManagement(target_dir=r'/home/pi/Documents/Images/',
                                          first_dir_name="Test0")
    img_dir.add()
    img_dir.debug(False)

    fps = modules.Fps()

    frame = modules.Frame(video_capture_index=0, side=300, name="Cam", filename="img",
                          limit_of_frames=30)

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

if __name__ == '__main__':
    main()
