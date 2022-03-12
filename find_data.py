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
"""This script will find a specified file in the specified directory"""

import os
from PIL import Image
import numpy as np
from find_data_utils import FindData

def main():
    """Main code"""
    FindData.InitBashArgs()
    args = FindData.InitBashArgs.get_args()

    input_file_path = args.input_file
    find_dir = args.find_dir

    img_format = "RGB"
    input_file = Image.open(input_file_path).convert(img_format)

    os.chdir(find_dir)

    for filename in FindData.Dataset.get_ordered_path(os.getcwd()):
        file_content = Image.open(filename).convert(img_format)

        if np.array_equal(input_file, file_content):
            print(filename)

if __name__ == '__main__':
    main()