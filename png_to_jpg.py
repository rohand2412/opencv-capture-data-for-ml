# Copyright (C) 2022  Rohan Dugad
#
# Contact info:
# https://docs.google.com/document/d/17IhBs4cz7FXphE0praCaWMjz016a7BFU5IQbm1CNnUc/edit?usp=sharing
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
