#!usr/bin/env python3
"""This script will display the data in the form of a slideshow"""

from modules import ModulesPackage

def main():
    """Main code"""
    keyboard = ModulesPackage.Keyboard()
    keyboard.start()

    while True:
        keyboard.consume()

    keyboard.stop()

if __name__ == '__main__':
    main()
