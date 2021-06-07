#!/usr/bin/env python3
"""This script contains all of the modules used in bgr_to_rgb.py"""

from raspberry_pi_libraries import multi_wrapper

class BgrToRgb(multi_wrapper.Packages):
    """Class that adapts parent's modules for BgrToRgb"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--input-dir", default=None, type=str,
                                     help="directory from which data will be converted")
            cls._parser.add_argument("--output-dir", default=None, type=str,
                                     help="directory at which converted data will be saved")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.input_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified. Please" \
                                                             + " specify '--input-dir' arguement")
            if not cls._args.output_dir:
                raise multi_wrapper.Packages.ArguementError(f"No output directory specified. Please" \
                                                             + " specify '--output-dir' argument")
            return cls._args
