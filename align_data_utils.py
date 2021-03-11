#!/usr/bin/env python3
"""This script contains all of the modules used in align_data.py"""

from raspberry_pi_libraries import multi_wrapper

class AlignData(multi_wrapper.Packages):
    """Class that adapts parent's modules for AlignData"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--labels-dir", default=None, type=str,
                                     help="directory with current labels")
            cls._parser.add_argument("--new-labels-dir", default=None, type=str,
                                     help="directory at which aligned labels will be saved")
            cls._parser.add_argument("--backup-images-dir", default=None, type=str,
                                     help="directory with old backup of images whose filenames" \
                                          + " align with the current labels")
            cls._parser.add_argument("--images-dir", default=None, type=str,
                                     help="directory with current unaligned images")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.labels_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--labels-dir'" \
                                                             + "arguement")
            if not cls._args.new_labels_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--new-labels-dir'" \
                                                             + "arguement")
            if not cls._args.backup_images_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--backup-images-dir'" \
                                                             + "arguement")
            if not cls._args.images_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--images-dir'" \
                                                             + "arguement")
            return cls._args
