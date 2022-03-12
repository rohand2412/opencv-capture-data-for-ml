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
"""This script rapidly capture images and stores them for later labeling and usage as data"""

import cv2
from capture_data_utils import CaptureData

def main():
    """Main code"""
    CaptureData.InitBashArgs()
    args = CaptureData.InitBashArgs.get_args()

    img_dir = CaptureData.DirectoryManagement.WriteDir(target_dir=args.target_dir,
                                                       first_dir_name="Test0")
    img_dir.add()
    img_dir.debug(False)

    fps = CaptureData.Fps()

    frame = CaptureData.Frame(side=300, name="Cam", filename=args.filename, limit_of_frames=args.limit_of_frames)

    try:
        while True:
            with fps.time_this():
                frame.capture_frame()
                frame.preprocessing()
                frame.imshow()
                frame.update()

                CaptureData.check_for_quit_request()

    except CaptureData.Break:
        frame.get_camera().close()
        cv2.destroyAllWindows()

        fps.calculate(frame.get_num())
        fps.debug(False)
        fps.print_fps()

        frame.export_buffer()

if __name__ == '__main__':
    main()
