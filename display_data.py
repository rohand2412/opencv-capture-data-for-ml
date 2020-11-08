#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

import pynput
import modules
import time

def main():
    """Main code"""
    keyboard = modules.Keyboard()
    keyboard.start()

    while True:
        # pressed = keyboard.get_pressed(True)
        # released = keyboard.get_pressed(True)

        # pressed = keyboard.get_pressed(False)
        # pressed_buffer = pressed.get_buffer()
        # pressed_len = pressed.get_len()
        # if pressed_len is not 0:
        #     print(pressed_buffer)
        # released = keyboard.get_released(False)
        # released_buffer = released.get_buffer()
        # released_len = released.get_len()
        # keyboard.empty_buffers()
        # if pressed_len is not 0:
        #     print(pressed_buffer)

        # for i in range(pressed_len):
        #     print(pressed_len)
        #     print(pressed_buffer[i])
        #     try:
        #         print("the {} was pressed  -- {}".format(pressed_buffer[i].name, pressed_len))
        #     except AttributeError:
        #         print(pressed_buffer)
        #         while True: pass
        # for i in range(released_len):
        #     print(released_len)
        #     print(released_buffer[i])
        #     try:
        #         print("the {} was released -- {}".format(released_buffer[i].name, released_len))
        #     except AttributeError:
        #         print(released_buffer)
        #         while True: pass

        # keyboard.empty_buffers()




        pressed = keyboard.get_pressed(True)
        pressed_buffer = pressed.get_buffer()
        pressed_len = pressed.get_len()
        released = keyboard.get_released(True)
        released_buffer = released.get_buffer()
        released_len = released.get_len()

        for col in range(pressed_len):
            if pressed_buffer[col]:
                print("pressed the {} key".format(pressed_buffer[col].name))
        for col in range(released_len):
            if released_buffer[col]:
                print("released the {} key".format(released_buffer[col].name))
        time.sleep(0.01)





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
