#!/usr/bin/env python3
"""This script will fix the filepaths in the specified xmls to be their current file location"""

import os
import xml.etree.ElementTree as ET
from fix_filepath_xml_utils import FixFilepathXML

def main():
    """Main code"""
    FixFilepathXML.InitBashArgs()
    args = FixFilepathXML.InitBashArgs.get_args()

    xml_dir = args.xml_dir
    img_dir = args.images_dir
    img_ext = os.path.splitext(os.listdir(img_dir)[0])[1]

    for filename in FixFilepathXML.Dataset.get_ordered_path(xml_dir):
        text = os.path.splitext(filename)[0]

        mytree = ET.parse(xml_dir + filename)
        myroot = mytree.getroot()

        for path in myroot.iter('path'):
            path.text = img_dir + text + img_ext

        for xml_filename in myroot.iter('filename'):
            xml_filename.text = text + img_ext

        mytree.write(xml_dir + filename)

if __name__ == '__main__':
    main()
