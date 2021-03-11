#!/usr/bin/env python3
"""This script will find the duplicate data between two directories"""

import subprocess
from find_duplicate_data_utils import FindDuplicateData

def main():
    """Main code"""
    FindDuplicateData.InitBashArgs()
    args = FindDuplicateData.InitBashArgs.get_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    for filename in FindDuplicateData.Dataset.get_ordered_path(input_dir):
        output = subprocess.check_output("python3 find_data.py " \
                                        + "--input-file " + input_dir + filename + " " \
                                        + "--find-dir " + output_dir, shell=True)

        output = output.decode()
        output = output.replace("\n", " ").split(" ")
        output = [item for item in output if item != ""]

        if len(output) > 1:
            print(output)

if __name__ == '__main__':
    main()
