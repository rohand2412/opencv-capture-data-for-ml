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
"""This script will remove the specified data and export the new set"""

import os
from PIL import Image
from remove_data_utils import RemoveData

def main():
    """Main code"""
    RemoveData.InitBashArgs()
    args = RemoveData.InitBashArgs.get_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    trash_dir = args.trash_dir
    remove_ids = args.remove_ids

    os.chdir(input_dir)

    img_format = "RGB"

    for filename in RemoveData.Dataset.get_ordered_path(os.getcwd()):
        file_num = int(''.join(filter(str.isdigit, filename)))
        data = Image.open(filename).convert(img_format)
        text = ''.join(filter(str.isalpha, os.path.splitext(filename)[0]))
        ext = os.path.splitext(filename)[1]

        if file_num not in remove_ids:
            data.save(output_dir + text + str(file_num) + ext)
        elif file_num in remove_ids:
            data.save(trash_dir + text + str(file_num) + ext)

if __name__ == '__main__':
    main()
