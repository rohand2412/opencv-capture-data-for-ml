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
"""This script will align the specified labels to their corresponding images"""

import os
import subprocess
import numpy as np
from align_data_utils import AlignData

def main():
    """Main code"""
    AlignData.InitBashArgs()
    args = AlignData.InitBashArgs.get_args()

    labels_dir = args.labels_dir
    new_labels_dir = args.new_labels_dir
    backup_dir = args.backup_images_dir
    images_dir = args.images_dir

    labels_ext = os.path.splitext(os.listdir(labels_dir)[0])[1]
    backup_ext = os.path.splitext(os.listdir(backup_dir)[0])[1]

    used_filenames = np.chararray([len(os.listdir(images_dir))], 10)
    used_filenames[:] = ""
    used_filenames_len = 0

    for filename in AlignData.Dataset.get_ordered_path(labels_dir):
        text = os.path.splitext(filename)[0]

        output = subprocess.check_output("python3 find_data.py " \
                                        + "--input-file " + backup_dir + text + backup_ext + " " \
                                        + "--find-dir " + images_dir, shell=True)

        output = output.decode()
        output = output.replace("\n", " ").split(" ")
        output = [item for item in output if item != ""]

        if not output:
            os.system("cp " + labels_dir + filename + " " + new_labels_dir + "outdated_" + filename)
        else:
            if output[0].encode() not in used_filenames:
                output_text = os.path.splitext(output[0])[0]
                os.system("cp " + labels_dir + filename + " " + new_labels_dir + output_text + labels_ext)
                used_filenames[used_filenames_len] = output[0]
                used_filenames_len += 1
            else:
                os.system("cp " + labels_dir + filename + " " + new_labels_dir + "duplicate_" + filename)

if __name__ == '__main__':
    main()
