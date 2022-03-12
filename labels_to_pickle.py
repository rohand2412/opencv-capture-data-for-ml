# Copyright (C) 2022  Rohan Dugad
#
# Contact info:
# https://docs.google.com/document/d/17IhBs4cz7FXphE0praCaWMjz016a7BFU5IQbm1CNnUc/edit?usp=sharing
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3
"""This script converts a column of a csv of labels to a single pickle pickle file"""

import pickle
import pandas as pd
from labels_to_pickle_utils import LabelsToPickle

def main():
    """Main code"""
    LabelsToPickle.InitBashArgs()
    args = LabelsToPickle.InitBashArgs.get_args()

    labels_path = args.labels_path
    output_path = args.output_path
    column_name = args.column_name

    df = pd.read_csv(labels_path, index_col=0)

    labels = df[column_name].to_numpy()

    pickle_out = open(output_path + "labels.pickle", "wb")
    pickle.dump(labels, pickle_out)
    pickle_out.close()

if __name__ == '__main__':
    main()
