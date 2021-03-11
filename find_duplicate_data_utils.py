#!/usr/bin/env python3
"""This script contains all of the modules used in find_duplicate_data.py"""

import base_utils

class FindDuplicateData(base_utils.Packages):
    """Class that adapts parent's modules for FindDuplicateData"""
    class InitBashArgs(base_utils.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the arguement parameters"""
            cls._parser.add_argument("--input-dir", default=None, type=str,
                                      help="directory with files to be searched for")
            cls._parser.add_argument("--output-dir", default=None, type=str,
                                      help="directory in which data will be searched")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.input_dir:
                raise base_utils.Packages.ArguementError(f"No input directory specified. Please" \
                                                          + " specify '--input-dir' arguement")
            if not cls._args.output_dir:
                raise base_utils.Packages.ArguementError(f"No output directory specified. Please" \
                                                          + " specify '--output-dir' argument")

            return cls._args
