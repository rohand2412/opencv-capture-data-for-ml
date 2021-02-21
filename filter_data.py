#!/usr/bin/env python3
"""This script will filter the data by division and export it"""

import os
from PIL import Image
from filter_data_utils import FilterData

def main():
    """Main code"""
    FilterData.InitBashArgs()
    args = FilterData.InitBashArgs.get_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    filter_factor = args.filter_factor

    os.chdir(input_dir)

    file_num = 0
    for folder in os.listdir():
        file_num += len(os.listdir(folder))
    file_num = file_num // filter_factor

    file_id = 0
    file_paths = [None for filename in range(file_num)]
    for folder in FilterData.Dataset.get_ordered_path(os.getcwd()):
        for filename in FilterData.Dataset.get_ordered_path(folder):
            if not file_id % filter_factor:
                file_paths[file_id // filter_factor] = folder + '/' + filename
            file_id += 1

    file_format = "RGB"
    file_new_format = ".png"
    for filename in range(file_num):
        if file_paths[filename]:
            data = Image.open(file_paths[filename]).convert(file_format)
            text = ''.join(filter(str.isalpha, os.path.splitext(os.path.basename(file_paths[filename]))[0]))
            data.save(output_dir + text + str(filename + 1) + file_new_format)

if __name__ == '__main__':
    main()
