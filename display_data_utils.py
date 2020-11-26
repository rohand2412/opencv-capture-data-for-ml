#!/usr/bin/env python3
"""This script contains all of the modules used in display_data.py"""

import modules

class DisplayData(modules.ModulesPackage):
    """Class that adapts parents modules for DisplayData"""
    class InitBashArgs(modules.ModulesPackage.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper"""
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--data-dir", default="Test0", type=str,
                                     help="directory from which data will be displayed")
