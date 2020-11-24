#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import time
import cv2
from display_data_utils import DisplayData

def nothing():
    print("nothing")

def main():
    """Main code"""
    timer = DisplayData.Timer(callback=nothing, delay_ms=500)
    timer.start()

    while not timer.update():
        pass

    print(timer.get_elapsed_time())

if __name__ == '__main__':
    main()
