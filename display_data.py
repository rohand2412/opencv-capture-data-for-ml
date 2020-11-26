#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import cv2
from display_data_utils import DisplayData

def main():
    """Main code"""
    DisplayData.InitBashArgs()
    args = DisplayData.InitBashArgs.get_args()

    img_dir = DisplayData.DirectoryManagement.ReadDir(target_dir=args.target_dir,
                                                      mode=DisplayData.READDIR_SLIDESHOW_MODE_KEYBOARD)
    img_dir.read()

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
