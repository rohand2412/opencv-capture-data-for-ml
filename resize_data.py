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
"""
This script will crop all the specified images to a square
and then resize them to a specified side length
"""

import cv2
from resize_data_utils import ResizeData

def main():
    """Main code"""
    ResizeData.InitBashArgs()
    args = ResizeData.InitBashArgs.get_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    NEW_IMAGE_SIZE = args.new_size

    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480

    for filename in ResizeData.Dataset.get_ordered_path(input_dir):
        data = cv2.imread(input_dir + filename)

        data = data[(FRAME_HEIGHT - FRAME_HEIGHT) // 2:
                    ((FRAME_HEIGHT - FRAME_HEIGHT) // 2) + FRAME_HEIGHT,
                    (FRAME_WIDTH - FRAME_HEIGHT) // 2:
                    ((FRAME_WIDTH - FRAME_HEIGHT) // 2) + FRAME_HEIGHT]

        data = cv2.resize(data, (NEW_IMAGE_SIZE, NEW_IMAGE_SIZE))

        cv2.imwrite(output_dir + filename, data)

if __name__ == '__main__':
    main()