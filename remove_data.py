#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import numpy as np
from PIL import Image


# In[ ]:


input_dir = '/home/rohan/Documents/RCJ2021Repos/raspberry-pi-images-rcj/Evac-Filtered-Images/'
output_dir = '/home/rohan/Documents/RCJ2021Repos/raspberry-pi-images-rcj/Evac-Final-Images/'

os.chdir(input_dir)


# In[ ]:


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

print(getOrderedPath(os.getcwd()))


# In[ ]:


remove_data = [1, 2, 2758]


# In[ ]:


filenames = getOrderedPath(os.getcwd())
file_total_num = len(filenames)

cur_file_index = 0
file_index_threshold = 1
img_format = "RGB"

while last_file_num < file_total_num:
    file_num = int(''.join(filter(str.isdigit, filenames[cur_file_index])))

    if file_num in remove_data:
        file_num = last_file_num + 1
    else:
        if (file_num - last_file_num) != 1:
            image = Image.open(img_paths[img]).convert(img_format)
            text = ''.join(filter(str.isalpha, os.path.splitext(filenames[cur_file_index])[0]))
            file_num = last_file_num + 1
            ext = os.path.splitext(filenames[cur_file_index])[1]
            image.save(output_dir + text + str(file_num) + ext)
        
    last_file_num = file_num
    cur_file_index += 1


# In[ ]:


file_id = 1
img_format = "RGB"

for filename in getOrderedPath(os.getcwd()):
    file_num = int(''.join(filter(str.isdigit, filename)))

    if file_num not in remove_data:
        data = Image.open(filename).convert(img_format)
        text = ''.join(filter(str.isalpha, os.path.splitext(filename)[0]))
        ext = os.path.splitext(filename)[1]
        data.save(output_dir + text + str(file_id) + ext)
        file_id += 1


# In[ ]:




