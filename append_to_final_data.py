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
"""This script append one directory's images with another directory and preserve the image ids"""

import os
import shutil
from append_to_final_data_utils import AppendToFinalData

def main():
    """Main code"""
    AppendToFinalData.InitBashArgs()
    args = AppendToFinalData.InitBashArgs.get_args()

    primary_final_dir = args.primary_final_dir
    secondary_final_dir = args.secondary_final_dir

    largest_digit = int(''.join(filter(str.isdigit, AppendToFinalData.Dataset.get_ordered_path(primary_final_dir)[-1])))

    text = ''.join(filter(str.isalpha, os.path.splitext(os.listdir(primary_final_dir)[0])[0]))
    ext = os.path.splitext(os.listdir(secondary_final_dir)[0])[1]

    for filename in AppendToFinalData.Dataset.get_ordered_path(secondary_final_dir):
        digit = int(''.join(filter(str.isdigit, filename))) + largest_digit

        shutil.copyfile(secondary_final_dir + filename, primary_final_dir + text + str(digit) + ext)

if __name__ == '__main__':
    main()
