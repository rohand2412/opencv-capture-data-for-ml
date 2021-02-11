#!/usr/bin/env python3
"""This script contains all of the modules used in display_data.py"""

import base_utils

class DisplayData(base_utils.Packages):
    """Class that adapts parents modules for DisplayData"""
    class InitBashArgs(base_utils.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper"""
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--target-dir", default="/home/pi/Documents/Images/Test0",
                                     type=str, help="directory from which data will be displayed")
            cls._parser.add_argument("--slideshow-mode",
                                     default=base_utils.Packages.READDIR_SLIDESHOW_MODE_KEYBOARD,
                                     type=str,
                                     help="mode of slidshow interface: either delay or keyboard input")
