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
"""This script will utilize the specified tflite model to display objects in the camera stream"""

import tflite_runtime.interpreter as tflite

import cv2
import numpy as np
from PIL import Image

from raspberry_pi_libraries import multi_wrapper, camera_wrapper

def main():
    """Main code"""
    model_path = "/path/to/model.tflite"

    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    _, input_height, input_width, _ = input_details[0]['shape']

    frame = camera_wrapper.Packages.Frame("Cam", img_format="rgb")

    try:
        while True:
            frame.capture_frame()
            image = frame.get_frame()

            image = image[(frame.get_height() - frame.get_height()) // 2:
                          ((frame.get_height() - frame.get_height()) // 2) + frame.get_height(),
                          (frame.get_width() - frame.get_height()) // 2:
                          ((frame.get_width() - frame.get_height()) // 2) + frame.get_height()]

            image = cv2.resize(image, (input_width, input_height))
            image = cv2.flip(image, -1)

            image_input = np.expand_dims(image, axis=0).astype(np.float32)

            image_input = image_input/255.0

            interpreter.set_tensor(input_details[0]['index'], image_input)
            interpreter.invoke()

            output = interpreter.get_tensor(output_details[0]['index'])[0][0]

            print(round(output))

            image = cv2.resize(image, (input_width * 4, input_height * 4))

            cv2.imshow("image", image)
            
            multi_wrapper.Packages.check_for_quit_request()
    
    except multi_wrapper.Packages.Break:
        frame.get_camera().close()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()