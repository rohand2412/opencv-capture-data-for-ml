#!/usr/bin/env python3
"""This script contains all of the modules used in png_to_jpg.py"""

from raspberry_pi_libraries import multi_wrapper

class PngToJpg(multi_wrapper.Packages):
    """Class that adapts parent's modules for PngToJpg"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--png-dir", default=None, type=str,
                                     help="directory with pngs")
            cls._parser.add_argument("--jpg-dir", default=None, type=str,
                                     help="directory where jpgs should be saved")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.png_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--png-dir'" \
                                                             + "arguement")
            if not cls._args.jpg_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--jpg-dir'" \
                                                             + "arguement")
            return cls._args
