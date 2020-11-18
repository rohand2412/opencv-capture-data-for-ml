#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

from display_data_utils import DisplayData

def main():
    """Main code"""
    keyboard = DisplayData.Keyboard()
    keyboard.start()

    while True:
        keyboard.consume()

    keyboard.stop()

if __name__ == '__main__':
    main()
