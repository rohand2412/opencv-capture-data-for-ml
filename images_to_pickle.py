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
"""This script converts a directory of images to a single pickle file"""

import os
import pickle
import numpy as np
import cv2
from images_to_pickle_utils import ImagesToPickle

def main():
    """Main code"""
    ImagesToPickle.InitBashArgs()
    args = ImagesToPickle.InitBashArgs.get_args()

    images_dir = args.images_dir
    save_dir = args.output_path
    image_size = args.image_size

    images = [None for image in os.listdir(images_dir)]

    for i, filename in enumerate(ImagesToPickle.Dataset.get_ordered_path(images_dir)):
        images[i] = cv2.imread(images_dir + filename)
        images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
        images[i] = cv2.resize(images[i], (image_size, image_size))

    images = np.array(images).reshape(-1, image_size, image_size, 3)

    pickle_out = open(save_dir + "images.pickle", "wb")
    pickle.dump(images, pickle_out)
    pickle_out.close()

if __name__ == '__main__':
    main()
