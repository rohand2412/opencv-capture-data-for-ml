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
"""This script contains all of the modules used in labels_to_pickle.py"""

from raspberry_pi_libraries import multi_wrapper

class LabelsToPickle(multi_wrapper.Packages):
    """Class that adapts parent's modules for LabelsToPickle"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--labels-path", default=None, type=str,
                                     help="path to csv file")
            cls._parser.add_argument("--output-path", default=None, type=str,
                                     help="path where to save pickle file")
            cls._parser.add_argument("--column-name", default=None, type=str,
                                     help="column in csv that contains the labels")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.labels_path:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--images-dir'" \
                                                             + "arguement")
            if not cls._args.output_path:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--output-path'" \
                                                             + "arguement")
            if not cls._args.column_name:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--column-name'" \
                                                             + "arguement")
            return cls._args
