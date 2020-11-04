#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import cv2
import modules

def main():
    """Main code"""
    img_dir = modules.DirectoryManagement.ReadDir(target_dir=r'/home/pi/Documents/Images/Test8')
    img_dir.read()

    try:
        while True:
            img_dir.imshow()
            img_dir.update(250)

    except modules.Break:
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
