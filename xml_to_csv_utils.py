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
"""This script contains all of the modules used in xml_to_csv.py"""

from raspberry_pi_libraries import multi_wrapper

class XmlToCsv(multi_wrapper.Packages):
    """Class that adapts parent's modules for AlignData"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--test-xml-dir", default=None, type=str,
                                     help="directory with test xmls")
            cls._parser.add_argument("--train-xml-dir", default=None, type=str,
                                     help="directory with train xmls")
            cls._parser.add_argument("--csv-dir", default=None, type=str,
                                     help="directory where csv will be stored")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.test_xml_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--test-xml-dir'" \
                                                             + "arguement")
            if not cls._args.train_xml_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--train-xml-dir'" \
                                                             + "arguement")
            if not cls._args.csv_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--csv-dir'" \
                                                             + "arguement")
            return cls._args
