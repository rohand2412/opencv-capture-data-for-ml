#!/usr/bin/env python3
"""This script append one directory's images with another directory and preserve the image ids"""

import os
import shutil
from append_to_final_data_utils import AppendToFinalData

def main():
    """Main code"""
    AppendToFinalData.InitBashArgs()
    args = AppendToFinalData.InitBashArgs.get_args()

    primary_final_dir = args.primary_final_dir
    secondary_final_dir = args.secondary_final_dir

    largest_digit = int(''.join(filter(str.isdigit, AppendToFinalData.Dataset.get_ordered_path(primary_final_dir)[-1])))

    text = ''.join(filter(str.isalpha, os.path.splitext(os.listdir(primary_final_dir)[0])[0]))
    ext = os.path.splitext(os.listdir(secondary_final_dir)[0])[1]

    for filename in AppendToFinalData.Dataset.get_ordered_path(secondary_final_dir):
        digit = int(''.join(filter(str.isdigit, filename))) + largest_digit

        shutil.copyfile(secondary_final_dir + filename, primary_final_dir + text + str(digit) + ext)

if __name__ == '__main__':
    main()
