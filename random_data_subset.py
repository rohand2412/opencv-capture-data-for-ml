#!/usr/bin/env python3
"""This script will save a random subset of the data for training on a smaller set"""

import os
import shutil
import random
from random_data_subset_utils import RandomDataSubset

def main():
    """Main code"""
    RandomDataSubset.InitBashArgs()
    args = RandomDataSubset.InitBashArgs.get_args()

    full_images_dir = args.images_dir
    full_labels_dir = args.labels_dir
    subset_images_dir = args.subset_images_dir
    subset_labels_dir = args.subset_labels_dir
    subset_size = args.subset_size

    subset_num = []
    full_num = RandomDataSubset.Dataset.get_ordered_path(full_images_dir)

    for i, filename in enumerate(full_num):
        full_num[i] = int(''.join(filter(str.isdigit, filename)))

    for _ in range(subset_size):
        file_id = random.choice(full_num)
        full_num.remove(file_id)
        subset_num.append(file_id)

    image_ext = os.path.splitext(os.listdir(full_images_dir)[0])[1]
    label_ext = os.path.splitext(os.listdir(full_labels_dir)[0])[1]
    text = ''.join(filter(str.isalpha, os.path.splitext(os.listdir(full_images_dir)[0])[0]))

    for file_id in subset_num:
        shutil.copyfile(full_images_dir + text + str(file_id) + image_ext,
                        subset_images_dir + text + str(file_id) + image_ext)
        shutil.copyfile(full_labels_dir + text + str(file_id) + label_ext,
                        subset_labels_dir + text + str(file_id) + label_ext)

if __name__ == '__main__':
    main()
