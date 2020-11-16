#!/usr/bin/env python3
"""This script contains all of the modules used in capture_data.py"""

import numpy as np
import cv2
import modules

class CaptureData(modules.ModulesPackage):
    """Class that adapts parents modules for CaptureData"""
    class Frame(modules.ModulesPackage.Frame):
        """Keeps track of all data regarding the video stream"""
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

        def export_buffer(self):
            """Saves all the frames from the video stream using a consistent naming convention"""
            self._buffer = np.array(self._buffer)
            for index in range(len(self._buffer)):
                cv2.imwrite(self._filename + str(index+1) + ".jpg", self._buffer[index])
