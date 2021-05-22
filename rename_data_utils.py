#!/usr/bin/env python3
"""This script contains all of the modules used in rename_data.py"""

from raspberry_pi_libraries import multi_wrapper

class RenameData(multi_wrapper.Packages):
    """Class that adapts parent's modules for RenameData"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--input-dir", default=None, type=str,
                                     help="directory from which data will be renamed")
            cls._parser.add_argument("--new-name", default=None, type=str,
                                     help="name to rename files to")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.input_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified. Please" \
                                                             + " specify '--input-dir' arguement")
            if not cls._args.new_name:
                raise multi_wrapper.Packages.ArguementError(f"No new name specified. Please" \
                                                             + " specify '--new-name' argument")
            return cls._args
