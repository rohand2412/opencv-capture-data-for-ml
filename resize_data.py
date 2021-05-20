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