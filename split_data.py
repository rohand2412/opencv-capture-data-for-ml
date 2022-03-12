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
