#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import cv2
import modules
import pynput
import os
import time
import datetime
import numpy as np

pressed_buffer = np.array([None for i in range(32)])
pressed_buffer_len = 0
released_buffer = np.array([None for i in range(32)])
released_buffer_len = 0

def log_events(buffer, buffer_len, key):
    buffer[buffer_len] = key
    if buffer_len == len(buffer)-1:
        buffer[0] = None
        buffer = np.roll(buffer, -1)
    else:
        buffer_len += 1
    return buffer, buffer_len

def read_events(buffer, buffer_len, state):
    for i in range(buffer_len):
        print(state + " the {0} key".format(buffer[i]))
    buffer[:] = None
    buffer_len = 0
    return buffer, buffer_len

def on_press(key):
    global pressed_buffer_len, pressed_buffer
    pressed_buffer, pressed_buffer_len = log_events(pressed_buffer, pressed_buffer_len, key)

def on_release(key):
    global released_buffer_len, released_buffer
    released_buffer, released_buffer_len = log_events(released_buffer, released_buffer_len, key)

def main():
    listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    global pressed_buffer, pressed_buffer_len, released_buffer, released_buffer_len
    while True:
        pressed_buffer, pressed_buffer_len = read_events(pressed_buffer, pressed_buffer_len, "pressed")
        released_buffer, released_buffer_len = read_events(released_buffer, released_buffer_len, "released")
    
    listener.stop()

if __name__ == '__main__':
    main()
