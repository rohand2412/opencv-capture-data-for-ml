#!/usr/bin/env python3
"""This script will filter the data by division and export it"""

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

data_path = '/home/rohan/Documents/RCJ2021Repos/raspberry-pi-images-rcj/Evac/'
save_path = '/home/rohan/Documents/RCJ2021Repos/raspberry-pi-images-rcj/Evac-Final-Images/'
os.chdir(data_path)

def getOrderedPath(path):
    files = os.listdir(path)
    num_data_types = 3
    files_split = [[None for data_type in range(num_data_types)] for name in range(len(files))]

    for i, name in enumerate(files):
        text = ''.join(filter(str.isalpha, os.path.splitext(name)[0]))
        num = ''.join(filter(str.isdigit, name))
        ext = os.path.splitext(name)[1]
        files_split[i] = [text, num, ext]

    files_split = np.array(files_split)
    files_ordered = [None for name in range(len(files_split))]
    files_ordered_len = 0
    files_cur_index = 0
    while files_ordered_len < len(files_ordered):
        indices = np.where(files_split[:, 1]==str(files_cur_index))
        if len(indices[0]) == 1:
            files_ordered[files_ordered_len] = files_split[indices[0][0]][0] + files_split[indices[0][0]][1] + files_split[indices[0][0]][2]
            files_ordered_len += 1
        elif indices[0].size > 0:
            while true:
                print("[ERROR] MULTIPLE DIRECTORIES WITH THE SAME ID")
        files_cur_index += 1
    
    return files_ordered

filter_factor = 5

img_num = 0

for folder in os.listdir():
    for img in os.listdir(folder):
        img_num += 1

img_num = img_num // filter_factor

img_paths = [None for img in range(img_num)]

img_id = 0

for folder in getOrderedPath(os.getcwd()):
    for img in getOrderedPath(folder):
        if not img_id % filter_factor:
            img_paths[img_id // filter_factor] = folder + "/" + img
        img_id += 1

display_photo = np.array(Image.open(img_paths[-1]))

fig, ax = plt.subplots(1)

ax.imshow(display_photo)

plt.show()

img_format = "RGB"

for img in range(img_num):
    if img_paths[img]:
        image = Image.open(img_paths[img]).convert(img_format)
        text = ''.join(filter(str.isalpha, os.path.splitext(os.path.basename(img_paths[img]))[0]))
        ext = os.path.splitext(os.path.basename(img_paths[img]))[1]
        image.save(save_path + text + str(img) + ext)
