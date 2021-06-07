#!/usr/bin/env python3
"""This script will convert data from bgr to rgb"""

import cv2
from bgr_to_rgb_utils import BgrToRgb

def main():
    """Main code"""
    BgrToRgb.InitBashArgs()
    args = BgrToRgb.InitBashArgs.get_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    for filename in BgrToRgb.Dataset.get_ordered_path(input_dir):
        data = cv2.imread(input_dir + filename)
        data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        cv2.imwrite(output_dir + filename, data)

if __name__ == '__main__':
    main()
