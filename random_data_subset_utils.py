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
"""This script contains all of the modules used in random_data_subset.py"""

from raspberry_pi_libraries import multi_wrapper

class RandomDataSubset(multi_wrapper.Packages):
    """Class that adapts parent's modules for RandomDataSubset"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--images-dir", default=None, type=str,
                                     help="directory with all images")
            cls._parser.add_argument("--subset-images-dir", default=None, type=str,
                                     help="directory wihere image subset is to be stored")
            cls._parser.add_argument("--labels-dir", default=None, type=str,
                                     help="directory with all labels")
            cls._parser.add_argument("--subset-labels-dir", default=None, type=str,
                                     help="directory where label subset is to be stored")
            cls._parser.add_argument("--subset-size", default=None, type=int,
                                     help="amount of data to be randomly selected")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.images_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--images-dir'" \
                                                             + "arguement")
            if not cls._args.subset_images_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--subset-images-dir'" \
                                                             + "arguement")
            if not cls._args.labels_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--labels-dir'" \
                                                             + "arguement")
            if not cls._args.subset_labels_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--subset-labels-dir'" \
                                                             + "arguement")
            if not cls._args.subset_size:
                raise multi_wrapper.Packages.ArguementError(f"No input number specified." \
                                                             + " Please specify '--subset-size'" \
                                                             + "arguement")
            return cls._args
