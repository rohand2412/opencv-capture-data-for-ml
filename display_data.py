#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import cv2
from display_data_utils import DisplayData

def main():
    """Main code"""
    DisplayData.InitBashArgs()
    args = DisplayData.InitBashArgs.get_args()
    print(args.data_dir)

if __name__ == '__main__':
    main()
