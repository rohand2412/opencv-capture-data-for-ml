#!/usr/bin/env python3
"""This script contains all of the modules used in filter_data.py"""

import os
import numpy as np
import base_utils

class FilterData(base_utils.Packages):
    """Class that adapts parent's modules for FilterData"""
    class ArguementError(Exception):
        """Used to report errors from InitBashArgs class"""

    class InitBashArgs(base_utils.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--input-dir", default=None, type=str,
                                     help="directory from which data will be filtered")
            cls._parser.add_argument("--output-dir", default=None, type=str,
                                     help="directory at which filtered data will be saved")
            cls._parser.add_argument("--filter-factor", default=5, type=int,
                                     help="divisor used in filtering process")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.input_dir:
                raise FilterData.ArguementError(f"No input directory specified. Please specify" \
                                                 + "'--input-dir' arguement")
            if not cls._args.output_dir:
                raise FilterData.ArguementError(f"No output directory specified. Please specify" \
                                                 + "'--output-dir' argument")
            return cls._args
