#!/usr/bin/env python3
"""This script will check that the specified labels match the specified images"""

import os
from check_data_utils import CheckData

def main():
    """Main code"""
    CheckData.InitBashArgs()
    args = CheckData.InitBashArgs.get_args()

    labels_dir = args.labels_dir
    images_dir = args.images_dir

    labels_ext = os.path.splitext(os.listdir(labels_dir)[0])[1]

    labels_names = os.listdir(labels_dir)
    images_names = os.listdir(images_dir)

    for filename in images_names:
        text = os.path.splitext(filename)[0]
        new_filename = text + labels_ext

        if new_filename not in labels_names:
            print(filename)

if __name__ == '__main__':
    main()
