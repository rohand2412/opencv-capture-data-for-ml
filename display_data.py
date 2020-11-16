#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import pynput
import modules
import time
import datetime

def main():
    """Main code"""
    print(datetime.datetime.now())
    keyboard = modules.Keyboard()
    print(datetime.datetime.now())
    keyboard.start()
    print(datetime.datetime.now())

    while True:
        # pressed = keyboard.get_pressed(True)
        # released = keyboard.get_pressed(True)

        index_of_val = modules.KEYBOARD_BUFFER_INDEX_OF_VAL
        pressed = keyboard.get_pressed()
        pressed_buffer = pressed.get_buffer()
        pressed_len = pressed.get_len()
        pressed_read_index = pressed.get_read_index()
        pressed_event_count = pressed.get_event_count()
        released = keyboard.get_released()
        released_buffer = released.get_buffer()
        released_len = released.get_len()
        released_read_index = released.get_read_index()
        released_event_count = released.get_event_count()

        while not (pressed_event_count[index_of_val] == 0):
            print("pressed_event_count -- ", pressed_event_count[index_of_val])

            event = pressed_buffer[pressed_read_index[index_of_val]]
            pressed.increment_read_index()
            pressed.decrement_event_count()
            try:
                print("the {} was pressed -- {}".format(event.name, pressed_event_count[index_of_val]))
            except AttributeError:
                print(pressed_buffer)
                while True: pass
        while not (released_event_count[index_of_val] == 0):
            print("released_event_count -- ", released_event_count[index_of_val])

            event = released_buffer[released_read_index[index_of_val]]
            released.increment_read_index()
            released.decrement_event_count()
            try:
                print("the {} was released -- {}".format(event.name, released_event_count[index_of_val]))
            except AttributeError:
                print(released_buffer)
                while True: pass
        # time.sleep(0.01)

        # keyboard.empty_buffers()




        # pressed = keyboard.get_pressed(True)
        # pressed_buffer = pressed.get_buffer()
        # pressed_len = pressed.get_len()
        # released = keyboard.get_released(True)
        # released_buffer = released.get_buffer()
        # released_len = released.get_len()

        # for col in range(pressed_len):
        #     print("pressed the {} key".format(pressed_buffer[col].name))
        # for col in range(released_len):
        #     print("released the {} key".format(released_buffer[col].name))
        # time.sleep(0.01)





        # buffer_rows = 8
        # buffer_cols = 4
        # pressed = keyboard.get_pressed(True)
        # pressed_buffer = pressed.get_buffer().reshape(buffer_rows, buffer_cols)
        # pressed_len = pressed.get_len()
        # released = keyboard.get_released(True)
        # released_buffer = released.get_buffer().reshape(buffer_rows, buffer_cols)
        # released_len = released.get_len()
        # # keyboard.empty_buffers()

        # if pressed_len is not 0 or released_len is not 0:
        #     print("\n\n\n")
        #     print("pressed " + str(pressed_len) + " \t\t\t\treleased " + str(released_len))
        #     for row in range(buffer_rows):
        #         for buffer in [pressed_buffer, released_buffer]:
        #             for col in range(buffer_cols):
        #                 if buffer[row][col]:
        #                     print(buffer[row][col].name, end=" ")
        #                 else:
        #                     print(buffer[row][col], end=" ")
        #             print("\t\t", end="")
        #         print()
        # time.sleep(0.01)

    keyboard.stop()

if __name__ == '__main__':
    main()
