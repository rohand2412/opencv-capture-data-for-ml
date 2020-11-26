#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import argparse
import cv2
from display_data_utils import DisplayData

def main():
    """Main code"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="Test0", type=str,
                        help="directory from which data will be displayed")
    args = parser.parse_args()
    print(args.data_dir)

if __name__ == '__main__':
    main()
