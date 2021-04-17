#!/usr/bin/env python3
"""This script contains all of the modules used in images_to_pickle.py"""

from raspberry_pi_libraries import multi_wrapper

class ImagesToPickle(multi_wrapper.Packages):
    """Class that adapts parent's modules for ImagesToPickle"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--images-dir", default=None, type=str,
                                     help="directory with labeled images")
            cls._parser.add_argument("--output-path", default=None, type=str,
                                     help="path where to save pickle file")
            cls._parser.add_argument("--image-size", default=None, type=int,
                                     help="size that images will be resized to")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.images_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--images-dir'" \
                                                             + "arguement")
            if not cls._args.output_path:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--output-path'" \
                                                             + "arguement")
            if not cls._args.image_size:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--image-size'" \
                                                             + "arguement")
            return cls._args
