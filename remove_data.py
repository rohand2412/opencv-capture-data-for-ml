#!/usr/bin/env python3
"""This script will remove the specified data and export the new set"""

import os
from PIL import Image
from remove_data_utils import RemoveData

def main():
    """Main code"""
    RemoveData.InitBashArgs()
    args = RemoveData.InitBashArgs.get_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    trash_dir = args.trash_dir
    remove_ids = args.remove_ids

    os.chdir(input_dir)

    file_id = 1
    img_format = "RGB"

    for filename in RemoveData.Dataset.get_ordered_path(os.getcwd()):
        file_num = int(''.join(filter(str.isdigit, filename)))
        data = Image.open(filename).convert(img_format)
        text = ''.join(filter(str.isalpha, os.path.splitext(filename)[0]))
        ext = os.path.splitext(filename)[1]

        if file_num not in remove_ids:
            data.save(output_dir + text + str(file_id) + ext)
            file_id += 1
        elif file_num in remove_ids:
            data.save(trash_dir + text + str(file_num) + ext)

if __name__ == '__main__':
    main()
