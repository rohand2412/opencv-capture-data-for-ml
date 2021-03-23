#!/usr/bin/env python3
"""This script will utilize the specified tflite model to display objects in the camera stream"""

import tflite_runtime.interpreter as tflite

import cv2
import numpy as np
from PIL import Image

from display_objects_utils import DisplayObjects

def main():
    """Main code"""
    DisplayObjects.InitBashArgs()
    args = DisplayObjects.InitBashArgs.get_args()

    model_path = args.model
    labels_path = args.labels

    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    _, input_height, input_width, _ = input_details[0]['shape']

    frame = DisplayObjects.Frame("Cam")

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

            image_input = np.expand_dims(image, axis=0)
            image_input = np.round(image_input).astype(np.uint8)

            interpreter.set_tensor(input_details[0]['index'], image_input)
            interpreter.invoke()

            boxes   = interpreter.get_tensor(output_details[0]['index'])
            classes = interpreter.get_tensor(output_details[1]['index'])
            scores  = interpreter.get_tensor(output_details[2]['index'])
            num     = interpreter.get_tensor(output_details[3]['index'])

            labels = ["dead", "alive"]

            for i in range(int(num[0])):
                if (((boxes[0][i][3] - boxes[0][i][1]) / (boxes[0][i][2] - boxes[0][i][0])) < 1.25) and scores[0][i] > 0.25:
                    scores[0][i] = np.round(scores[0][i] * 100) / 100
                    image = cv2.rectangle(image,
                                        (int(boxes[0][i][1]*input_width),
                                        int(boxes[0][i][0]*input_height)),
                                        (int(boxes[0][i][3]*input_width),
                                        int(boxes[0][i][2]*input_height)),
                                        (0, 0, 255), 1)
                    image = cv2.putText(image, labels[int(classes[0][i] + 0.5)],
                                        (int(boxes[0][i][1]*input_width),
                                        int(boxes[0][i][0]*input_height)),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),
                                        2, cv2.LINE_AA, False)
                    (_, text_height), _ = cv2.getTextSize(str(scores[0][i]),
                                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
                    image = cv2.putText(image, str(scores[0][i]),
                                        (int(boxes[0][i][1]*input_width),
                                        int(boxes[0][i][0]*input_height) + text_height + 2),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255),
                                        2, cv2.LINE_AA, False)

            image = cv2.resize(image, (input_width * 2, input_height * 2))

            cv2.imshow("image", image)
            
            DisplayObjects.check_for_quit_request()
    
    except DisplayObjects.Break:
        frame.get_camera().close()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()