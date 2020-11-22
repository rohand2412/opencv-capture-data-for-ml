#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import cv2
from display_data_utils import DisplayData

def main():
    """Main code"""
    img_dir = DisplayData.DirectoryManagement.ReadDir(target_dir=r'/home/pi/Documents/Images/Test8')
    img_dir.read()
    keyboard = DisplayData.Keyboard()
    keyboard.start()

    try:
        while True:
            img_dir.imshow()
            img_dir.update(250)

            keyboard.consume()

            DisplayData.check_for_quit_request()

    except DisplayData.Break:
        cv2.destroyAllWindows()
        keyboard.stop()

if __name__ == '__main__':
    main()
