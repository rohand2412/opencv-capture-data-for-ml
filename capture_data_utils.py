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
"""This script contains all of the modules used in capture_data.py"""

import picamera
import picamera.array
import time
import numpy as np
import cv2
from raspberry_pi_libraries import multi_wrapper
from raspberry_pi_libraries import camera_wrapper

class CaptureData(multi_wrapper.Packages):
    """Class that adapts parents modules for CaptureData"""
    class Fps(multi_wrapper.Packages.Fps):
        """Computes Fps over a series of frames and their times"""
        def calculate(self, frame_num):
            """Calculates the fps based upon a series of stats"""
            self._elapsed_times = np.delete(self._elapsed_times, [0])
            self._mean = np.sum(self._elapsed_times)/frame_num*1.0
            self._fps = 1.0 / self._mean

    class Frame(camera_wrapper.Packages.Frame):
        """Keeps track of all data regarding the video stream"""
        def __init__(self, name, side, filename, limit_of_frames=None):
            self._width = 640
            self._height = 480
            self._camera = picamera.PiCamera()
            self._camera.resolution = (self._width, self._height)
            self._camera.framerate = 32
            self._camera.start_preview()
            time.sleep(0.1)
            self._camera.stop_preview()
            self._name = name
            self._frame = np.array([])
            self._filename = filename
            self._side = side
            self._limit_of_frames = limit_of_frames
            self._num = 1
            self._duplicate_frame = False
            self._frame_orig = np.array([])

            if self._limit_of_frames:
                self._buffer = [None for i in range(self.get_limit_of_frames())]
            else:
                self._buffer = []

        def capture_frame(self):
            """Reads the frame from the video stream"""
            self._duplicate_frame = False

            frame = None
            with picamera.array.PiRGBArray(self._camera, size=(self._width, self._height)) as stream:
                self._camera.capture(stream, format="bgr", use_video_port=True)
                frame = stream.array

            if self._frame.any():
                if not (np.subtract(self._frame_orig, cv2.resize(frame, (320, 240))).any()):
                    self._duplicate_frame = True
            if not self._duplicate_frame:
                self._frame = frame
                self._frame_orig = cv2.resize(frame, (320, 240))

        def preprocessing(self):
            """Preprocesses the frame"""
            if not self._duplicate_frame:
                self._frame = cv2.flip(self._frame, -1)
                self._frame = self._frame[0:self._height,
                                          int((self._width-self._height)/2):
                                          int((self._width+self._height)/2)]

                if self._limit_of_frames:
                    self._buffer[self._num-1] = self._frame
                else:
                    self._buffer.append(self._frame)

        def update(self):
            if not self._duplicate_frame:
                if self._limit_of_frames:
                    if self._num >= self._limit_of_frames:
                        raise multi_wrapper.Packages.Break
                self._num += 1

        def export_buffer(self):
            """Saves all the frames from the video stream using a consistent naming convention"""
            self._buffer = np.array(self._buffer)
            for index in range(len(self._buffer)):
                cv2.imwrite(self._filename + str(index+1) + ".jpg", cv2.resize(self._buffer[index], (self._side, self._side)))

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

    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper"""
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--target-dir", default="/home/pi/Documents/Images/",
                                     type=str, help="directory from which data will be displayed")
            cls._parser.add_argument("--limit-of-frames", default=None, type=int,
                                     help="number of frames that will be captured")
            cls._parser.add_argument("--filename", default="img", type=str,
                                     help="name that will be used to save images")
