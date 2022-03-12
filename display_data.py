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

#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import cv2
from display_data_utils import DisplayData

def main():
    """Main code"""
    DisplayData.InitBashArgs()
    args = DisplayData.InitBashArgs.get_args()

    img_dir = DisplayData.DirectoryManagement.ReadDir(target_dir=args.target_dir,
                                                      mode=args.slideshow_mode)
    img_dir.read()

    try:
        while True:
            img_dir.imshow()
            img_dir.update()

            DisplayData.check_for_quit_request()

    except DisplayData.Break:
        cv2.destroyAllWindows()
        img_dir.close()

if __name__ == '__main__':
    main()
