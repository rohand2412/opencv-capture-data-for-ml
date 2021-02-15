#/usr/bin/env python3
"""This script contains all of the modules used in remove_data.py"""

import base_utils

class RemoveData(base_utils.Packages):
    """Class that adapts parent's modules for RemoveData"""
    class InitBashArgs(base_utils.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--input-dir", default=None, type=str,
                                     help="directory from which data will be removed")
            cls._parser.add_argument("--output-dir", default=None, type=str,
                                     help="directory at which pruned data will be saved")
            cls._parser.add_argument("--remove-ids", default=None, nargs='+', type=int,
                                     help="ids of data to be removed")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.input_dir:
                raise base_utils.Packages.ArguementError(f"No input directory specified. Please" \
                                                          + " specify '--input-dir' arguement")
            if not cls._args.output_dir:
                raise base_utils.Packages.ArguementError(f"No output directory specified. Please" \
                                                          + " specify '--output-dir' argument")
            if not cls._args.remove_ids:
                raise base_utils.Packages.ArguementError(f"No data to be removed specified." \
                                                          + " Please specify '--remove-ids'" \
                                                          + " arguement")
            return cls._args
