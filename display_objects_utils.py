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
"""This script contains all of the modules used in align_data.py"""

from raspberry_pi_libraries import multi_wrapper
from raspberry_pi_libraries import camera_wrapper

class DisplayObjects(multi_wrapper.Packages, camera_wrapper.Packages):
    """Class that adapts parent's modules for DisplayObjects"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--model", default=None, type=str,
                                     help="path to tflite model")
            cls._parser.add_argument("--labels", default=None, type=str,
                                     help="path to label map")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.model:
                raise multi_wrapper.Packages.ArguementError(f"No input path specified." \
                                                             + " Please specify '--model'" \
                                                             + "arguement")
            if not cls._args.labels:
                raise multi_wrapper.Packages.ArguementError(f"No input path specified." \
                                                             + " Please specify '--labels'" \
                                                             + "arguement")
            return cls._args
