#!/usr/bin/env python3
"""This script contains all of the modules used in labels_to_pickle.py"""

from raspberry_pi_libraries import multi_wrapper

class LabelsToPickle(multi_wrapper.Packages):
    """Class that adapts parent's modules for LabelsToPickle"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--labels-path", default=None, type=str,
                                     help="path to csv file")
            cls._parser.add_argument("--output-path", default=None, type=str,
                                     help="path where to save pickle file")
            cls._parser.add_argument("--column-name", default=None, type=str,
                                     help="column in csv that contains the labels")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.labels_path:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--images-dir'" \
                                                             + "arguement")
            if not cls._args.output_path:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--output-path'" \
                                                             + "arguement")
            if not cls._args.column_name:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--column-name'" \
                                                             + "arguement")
            return cls._args
