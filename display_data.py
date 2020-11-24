#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import cv2
from display_data_utils import DisplayData

def nothing():
    """Does nothing"""
    print("nothing")

def main():
    """Main code"""
    img_dir = DisplayData.DirectoryManagement.ReadDir(target_dir=r'/home/pi/Documents/Images/Test8',
                                                      mode=DisplayData.READDIR_SLIDESHOW_MODE_KEYBOARD)
    img_dir.read()
    timer = DisplayData.Timer(callback=nothing, delay_ms=500)
    timer.start()

    while not timer.update():
        pass

    print(timer.get_elapsed_time())

    try:
        while True:
            img_dir.imshow()
            img_dir.update()

            DisplayData.check_for_quit_request()

    except DisplayData.Break:
        cv2.destroyAllWindows()
        img_dir.close()

if __name__ == '__main__':
    main()
