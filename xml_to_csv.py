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
"""Converts directory of xmls into singular csv"""

import os
import glob
import xml.etree.ElementTree as ET
import pandas as pd
from xml_to_csv_utils import XmlToCsv

def xml_to_csv(path):
    """Returns pandas dataframe with xml data"""
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    """Main code"""
    XmlToCsv.InitBashArgs()
    args = XmlToCsv.InitBashArgs.get_args()

    test_xml_dir = args.test_xml_dir
    train_xml_dir = args.train_xml_dir
    csv_dir = args.csv_dir

    for i, directory in enumerate([train_xml_dir, test_xml_dir]):
        labels_dir = os.path.join(directory, "")
        xml_df = xml_to_csv(labels_dir)
        xml_df.to_csv(csv_dir + '{}_labels.csv'.format(["train", "test"][i]), index=None)

if __name__ == '__main__':
    main()
