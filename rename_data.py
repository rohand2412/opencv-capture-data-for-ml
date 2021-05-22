#!/usr/bin/env python3
"""This script will uniformalize the names of all the files in a directory"""

import os
from rename_data_utils import RenameData

def main():
    """Main code"""
    RenameData.InitBashArgs()
    args = RenameData.InitBashArgs.get_args()

    input_dir = args.input_dir
    new_name = args.new_name

    ext = os.path.splitext(os.listdir(input_dir)[0])[1]

    for filename in RenameData.Dataset.get_ordered_path(input_dir):
        digit = ''.join(filter(str.isdigit, filename))

        os.rename(input_dir + filename, input_dir + new_name + digit + ext)

if __name__ == '__main__':
    main()
