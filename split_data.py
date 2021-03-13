#!/usr/bin/env python3
"""This script performs the test and train splits of the data"""

import shutil
import random
from split_data_utils import SplitData

def main():
    """Main code"""
    SplitData.InitBashArgs()
    args = SplitData.InitBashArgs.get_args()

    images_dir = args.images_dir
    test_images_dir = args.test_images_dir
    train_images_dir = args.train_images_dir
    labels_dir = args.labels_dir
    test_labels_dir = args.test_labels_dir
    train_labels_dir = args.train_labels_dir

    images = SplitData.Dataset.get_ordered_path(images_dir)
    labels = SplitData.Dataset.get_ordered_path(labels_dir)

    possible_indices = list(range(10))
    first_index = random.choice(possible_indices)
    possible_indices.remove(first_index)
    second_index = random.choice(possible_indices)

    for file_id, _ in enumerate(images):
        if (file_id % 10 == first_index) or (file_id % 10 == second_index):
            shutil.copyfile(images_dir + images[file_id], test_images_dir + images[file_id])
            shutil.copyfile(labels_dir + labels[file_id], test_labels_dir + labels[file_id])
        else:
            shutil.copyfile(images_dir + images[file_id], train_images_dir + images[file_id])
            shutil.copyfile(labels_dir + labels[file_id], train_labels_dir + labels[file_id])

        if not file_id % 10:
            possible_indices = list(range(10))
            first_index = random.choice(possible_indices)
            possible_indices.remove(first_index)
            second_index = random.choice(possible_indices)

if __name__ == '__main__':
    main()
