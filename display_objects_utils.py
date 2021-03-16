#!/usr/bin/env python3
"""This script contains all of the modules used in align_data.py"""

from raspberry_pi_libraries import multi_wrapper
from raspberry_pi_libraries import camera_wrapper

class DisplayObjects(multi_wrapper.Packages, camera_wrapper.Packages):
    """Class that adapts parent's modules for DisplayObjects"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--model", default=None, type=str,
                                     help="path to tflite model")
            cls._parser.add_argument("--labels", default=None, type=str,
                                     help="path to label map")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.model:
                raise multi_wrapper.Packages.ArguementError(f"No input path specified." \
                                                             + " Please specify '--model'" \
                                                             + "arguement")
            if not cls._args.labels:
                raise multi_wrapper.Packages.ArguementError(f"No input path specified." \
                                                             + " Please specify '--labels'" \
                                                             + "arguement")
            return cls._args
