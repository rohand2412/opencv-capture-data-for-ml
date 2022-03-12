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
"""Uses provided tflite model to label provided data in an automated fashion"""

import os
import cv2
import numpy as np
import pandas as pd
import tflite_runtime.interpreter as tflite
from auto_angle_labeler_utils import AutoAngleLabeler

def main():
    """Main code"""
    AutoAngleLabeler.InitBashArgs()
    args = AutoAngleLabeler.InitBashArgs.get_args()

    model_path = args.model_path
    label_path = args.label_path
    images_dir = args.images_dir
    images_ext = os.path.splitext(os.listdir(images_dir)[0])[1]

    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_index = interpreter.get_input_details()[0]['index']
    output_index = interpreter.get_output_details()[0]['index']

    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

    labels = pd.read_csv(label_path, index_col=0)

    unlabeled = list(labels.index.where(labels['labeled'] == False))
    unlabeled = [label for label in unlabeled if label == label]

    for label in unlabeled:
        image = cv2.imread(images_dir + label + images_ext)
        image = cv2.resize(image, (input_width, input_height))

        image_in = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_in = np.expand_dims(image, axis=0).astype(np.float32)
        image_in = image_in/255.0

        interpreter.set_tensor(input_index, image_in)
        interpreter.invoke()
        angle = interpreter.get_tensor(output_index)[0][0]

        x_coord = None
        y_coord = 0
        if angle > 0:
            x_coord = input_width/2 + np.tan(np.deg2rad(abs(angle))) * input_height
        else:
            x_coord = input_width/2 - np.tan(np.deg2rad(abs(angle))) * input_height

        if x_coord < 0 or x_coord >= input_width:
            if angle > 0:
                x_coord = input_width - 1
            else:
                x_coord = 0
            y_coord = input_height - (input_width/2)/np.tan(np.deg2rad(abs(angle)))

        x_coord = int(min(max(round(x_coord), 0), input_width-1))
        y_coord = int(min(max(round(y_coord), 0), input_height-1))
        angle = round(angle * 100)/100

        labels.loc[label, "x"] = x_coord
        labels.loc[label, "y"] = y_coord
        labels.loc[label, "angle"] = angle
        labels.loc[label, "labeled"] = True

        print("labeled ", label)

    labels.to_csv(label_path)

if __name__ == '__main__':
    main()