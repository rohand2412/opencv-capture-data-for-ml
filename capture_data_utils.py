#!/usr/bin/env python3
"""This script contains all of the modules used in capture_data.py"""

import numpy as np
import cv2
import modules

class CaptureData(modules.ModulesPackage):
    """Class that adapts parents modules for CaptureData"""
    class Frame(modules.ModulesPackage.Frame):
        """Keeps track of all data regarding the video stream"""
        def __init__(self, name, side, filename, limit_of_frames=None):
            super().__init__(name)
            self._filename = filename
            self._side = side
            self._limit_of_frames = limit_of_frames
            self._num = 1

            if self._limit_of_frames:
                self._buffer = [None for i in range(self.get_limit_of_frames())]
            else:
                self._buffer = []

        def preprocessing(self):
            """Preprocesses the frame"""
            self._frame = cv2.flip(self._frame, 1)
            self._frame = self._frame[int((self._height-self._side)/2):
                                      int((self._height+self._side)/2),
                                      int((self._width-self._side)/2):
                                      int((self._width+self._side)/2)]

            if self._limit_of_frames:
                self._buffer[self._num-1] = self._frame
            else:
                self._buffer.append(self._frame)

        def update(self):
            if self._limit_of_frames:
                if self._num >= self._limit_of_frames:
                    raise modules.ModulesPackage.Break
            self._num += 1

        def export_buffer(self):
            """Saves all the frames from the video stream using a consistent naming convention"""
            self._buffer = np.array(self._buffer)
            for index in range(len(self._buffer)):
                cv2.imwrite(self._filename + str(index+1) + ".jpg", self._buffer[index])

        def get_filename(self):
            """Returns filename for saving frames"""
            return self._filename

        def get_side(self):
            """Returns cropped square side length"""
            return self._side

        def get_limit_of_frames(self):
            """Returns limit of frames for the video stream"""
            return self._limit_of_frames

        def get_num(self):
            """Returns running number of current frames"""
            return self._num

    class InitBashArgs(modules.ModulesPackage.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper"""
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--target-dir", default="/home/pi/Documents/Images/",
                                     type=str, help="directory from which data will be displayed")
