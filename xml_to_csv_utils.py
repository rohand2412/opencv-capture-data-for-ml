#!/usr/bin/env python3
"""This script contains all of the modules used in xml_to_csv.py"""

from raspberry_pi_libraries import multi_wrapper

class XmlToCsv(multi_wrapper.Packages):
    """Class that adapts parent's modules for AlignData"""
    class InitBashArgs(multi_wrapper.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--test-xml-dir", default=None, type=str,
                                     help="directory with test xmls")
            cls._parser.add_argument("--train-xml-dir", default=None, type=str,
                                     help="directory with train xmls")
            cls._parser.add_argument("--csv-dir", default=None, type=str,
                                     help="directory where csv will be stored")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.test_xml_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--test-xml-dir'" \
                                                             + "arguement")
            if not cls._args.train_xml_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--train-xml-dir'" \
                                                             + "arguement")
            if not cls._args.csv_dir:
                raise multi_wrapper.Packages.ArguementError(f"No input directory specified." \
                                                             + " Please specify '--csv-dir'" \
                                                             + "arguement")
            return cls._args
