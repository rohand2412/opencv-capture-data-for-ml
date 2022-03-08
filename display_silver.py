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