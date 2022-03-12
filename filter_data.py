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
"""This script will filter the data by division and export it"""

import os
from PIL import Image
from filter_data_utils import FilterData

def main():
    """Main code"""
    FilterData.InitBashArgs()
    args = FilterData.InitBashArgs.get_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    filter_factor = args.filter_factor

    os.chdir(input_dir)

    file_num = 0
    for folder in os.listdir():
        file_num += len(os.listdir(folder))
    file_num = file_num // filter_factor

    file_id = 0
    file_paths = [None for filename in range(file_num)]
    for folder in FilterData.Dataset.get_ordered_path(os.getcwd()):
        for filename in FilterData.Dataset.get_ordered_path(folder):
            if not file_id % filter_factor:
                file_paths[file_id // filter_factor] = folder + '/' + filename
            file_id += 1

    file_format = "RGB"
    file_new_format = ".png"
    for filename in range(file_num):
        if file_paths[filename]:
            data = Image.open(file_paths[filename]).convert(file_format)
            text = ''.join(filter(str.isalpha, os.path.splitext(os.path.basename(file_paths[filename]))[0]))
            data.save(output_dir + text + str(filename + 1) + file_new_format)

if __name__ == '__main__':
    main()
