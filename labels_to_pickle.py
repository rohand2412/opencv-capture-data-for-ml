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
