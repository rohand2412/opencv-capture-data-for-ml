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
"""This script will check that the specified labels match the specified images"""

import os
from check_data_utils import CheckData

def main():
    """Main code"""
    CheckData.InitBashArgs()
    args = CheckData.InitBashArgs.get_args()

    labels_dir = args.labels_dir
    images_dir = args.images_dir

    labels_ext = os.path.splitext(os.listdir(labels_dir)[0])[1]

    labels_names = os.listdir(labels_dir)
    images_names = os.listdir(images_dir)

    for filename in images_names:
        text = os.path.splitext(filename)[0]
        new_filename = text + labels_ext

        if new_filename not in labels_names:
            print(filename)

if __name__ == '__main__':
    main()
