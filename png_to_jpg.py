#!/usr/bin/env python3
"""This script will convert a directory of pngs to a directory of jpgs"""

import os
from PIL import Image
from png_to_jpg_utils import PngToJpg

def main():
    """Main code"""
    PngToJpg.InitBashArgs()
    args = PngToJpg.InitBashArgs.get_args()

    png_dir = args.png_dir
    jpg_dir = args.jpg_dir

    new_file_format = ".jpg"
    image_format = "RGB"

    for filename in PngToJpg.Dataset.get_ordered_path(png_dir):
        data = Image.open(png_dir + filename).convert(image_format)
        text = os.path.splitext(filename)[0]
        data.save(jpg_dir + text + new_file_format)

if __name__ == '__main__':
    main()
