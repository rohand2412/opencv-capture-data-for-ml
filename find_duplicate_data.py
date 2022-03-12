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
"""This script will find the duplicate data between two directories"""

import subprocess
from find_duplicate_data_utils import FindDuplicateData

def main():
    """Main code"""
    FindDuplicateData.InitBashArgs()
    args = FindDuplicateData.InitBashArgs.get_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    for filename in FindDuplicateData.Dataset.get_ordered_path(input_dir):
        output = subprocess.check_output("python3 find_data.py " \
                                        + "--input-file " + input_dir + filename + " " \
                                        + "--find-dir " + output_dir, shell=True)

        output = output.decode()
        output = output.replace("\n", " ").split(" ")
        output = [item for item in output if item != ""]

        if len(output) > 1:
            print(output)

if __name__ == '__main__':
    main()
