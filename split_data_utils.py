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
"""This script contains all of the modules used in split_data.py"""

from raspberry_pi_libraries import multi_wrapper

class SplitData(multi_wrapper.Packages):
    """Class that adapts parent's modules for SplitData"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--images-dir", default=None, type=str,
                                     help="directory with current images")
            cls._parser.add_argument("--test-images-dir", default=None, type=str,
                                     help="directory where test images are to be saved")
            cls._parser.add_argument("--train-images-dir", default=None, type=str,
                                     help="directory where train images are to be saved")
            cls._parser.add_argument("--labels-dir", default=None, type=str,
                                     help="directory with current labels")
            cls._parser.add_argument("--test-labels-dir", default=None, type=str,
                                     help="directory where test labels are to be saved")
            cls._parser.add_argument("--train-labels-dir", default=None, type=str,
                                     help="directory where train labels are to be saved")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.images_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--images-dir'" \
                                                             + "arguement")
            if not cls._args.test_images_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--test-images-dir'" \
                                                             + "arguement")
            if not cls._args.train_images_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--train-images-dir'" \
                                                             + "arguement")
            if not cls._args.labels_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--labels-dir'" \
                                                             + "arguement")
            if not cls._args.test_labels_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--test-labels-dir'" \
                                                             + "arguement")
            if not cls._args.train_labels_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--train-labels-dir'" \
                                                             + "arguement")
            return cls._args
