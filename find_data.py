#!/usr/bin/env python3
"""This script will find a specified file in the specified directory"""

import os
from PIL import Image
import numpy as np
from find_data_utils import FindData

def main():
    """Main code"""
    FindData.InitBashArgs()
    args = FindData.InitBashArgs.get_args()

    input_file_path = args.input_file
    find_dir = args.find_dir

    img_format = "RGB"
    input_file = Image.open(input_file_path).convert(img_format)

    os.chdir(find_dir)

    for filename in FindData.Dataset.get_ordered_path(os.getcwd()):
        file_content = Image.open(filename).convert(img_format)

        if np.array_equal(input_file, file_content):
            print(filename)
            break

if __name__ == '__main__':
    main()