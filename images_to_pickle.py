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
