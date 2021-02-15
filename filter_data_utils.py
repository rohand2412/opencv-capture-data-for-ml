#!/usr/bin/env python3
"""This script contains all of the modules used in filter_data.py"""

import os
import numpy as np
import base_utils

class FilterData(base_utils.Packages):
    """Class that adapts parent's modules for FilterData"""
    @staticmethod
    def get_ordered_path(path):
        """Returns list of all items in specified path in numerical order"""
        files = os.listdir(path)
        num_data_types = 3
        files_split = [[None for data_type in range(num_data_types)] for name in range(len(files))]

        for i, name in enumerate(files):
            text = ''.join(filter(str.isalpha, os.path.splitext(name)[0]))
            num = ''.join(filter(str.isdigit, name))
            ext = os.path.splitext(name)[1]
            files_split[i] = [text, num, ext]

        files_split = np.array(files_split)
        files_ordered = [None for name in range(len(files_split))]
        files_ordered_len = 0
        files_cur_index = 0
        while files_ordered_len < len(files_ordered):
            indices = np.where(files_split[:, 1]==str(files_cur_index))
            if len(indices[0]) == 1:
                files_ordered[files_ordered_len] = files_split[indices[0][0]][0] \
                                                   + files_split[indices[0][0]][1] \
                                                   + files_split[indices[0][0]][2]
                files_ordered_len += 1
            elif indices[0].size > 0:
                while True:
                    print("[ERROR] MULTIPLE DIRECTORIES WITH THE SAME ID")
            files_cur_index += 1

        return files_ordered

    class ArguementError(Exception):
        """Used to report errors from InitBashArgs class"""

    class InitBashArgs(base_utils.Packages.InitBashArgs):
        """Initalizes the arguements present for bash execution which will be different for each
        application of this wrapper """
        @classmethod
        def get_arg_params(cls):
            """Returns the argument paramters"""
            cls._parser.add_argument("--input-dir", default=None, type=str,
                                     help="directory from which data will be filtered")
            cls._parser.add_argument("--output-dir", default=None, type=str,
                                     help="directory at which filtered data will be saved")
            cls._parser.add_argument("--filter-factor", default=5, type=int,
                                     help="divisor used in filtering process")

        @classmethod
        def get_args(cls):
            """Returns data inputted from bash"""
            if not cls._args.input_dir:
                raise FilterData.ArguementError(f"No input directory specified. Please specify" \
                                                 + "'--input-dir' arguement")
            if not cls._args.output_dir:
                raise FilterData.ArguementError(f"No output directory specified. Please specify" \
                                                 + "'--output-dir' argument")
            return cls._args
