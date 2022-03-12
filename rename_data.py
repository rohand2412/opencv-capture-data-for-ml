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
"""This script will uniformalize the names of all the files in a directory"""

import os
from rename_data_utils import RenameData

def main():
    """Main code"""
    RenameData.InitBashArgs()
    args = RenameData.InitBashArgs.get_args()

    input_dir = args.input_dir
    new_name = args.new_name

    ext = os.path.splitext(os.listdir(input_dir)[0])[1]

    for filename in RenameData.Dataset.get_ordered_path(input_dir):
        digit = ''.join(filter(str.isdigit, filename))

        os.rename(input_dir + filename, input_dir + new_name + digit + ext)

if __name__ == '__main__':
    main()
