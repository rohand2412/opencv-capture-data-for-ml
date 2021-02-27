#!/usr/bin/env python3
"""This script will display the ids of the trashed data"""

import os
from get_remove_data_utils import GetRemoveData

def main():
    """Main code"""
    GetRemoveData.InitBashArgs()
    args = GetRemoveData.InitBashArgs.get_args()

    trash_dir = args.trash_dir

    os.chdir(trash_dir)

    for filename in GetRemoveData.Dataset.get_ordered_path(os.getcwd()):
        print(''.join(filter(str.isdigit, filename)), " ")

if __name__ == '__main__':
    main()
