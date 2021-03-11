#!/usr/bin/env python3
"""This script contains all of the modules used in get_remove_data.py"""

from raspberry_pi_libraries import multi_wrapper

class GetRemoveData(multi_wrapper.Packages):
    """Class that adapts parent's modules for GetRemoveData"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the arguement parameters"""
            cls._parser.add_argument("--trash-dir", default=None, type=str,
                                      help="directory from ids will be displayed")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.trash_dir:
                raise multi_wrapper.Packages.ArguementError(f"No trash directory specified. Please" \
                                                          + " specify '--trash-dir' arguement")

            return cls._args
