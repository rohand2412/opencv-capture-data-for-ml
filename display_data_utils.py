#!/usr/bin/env python3
"""This script contains all of the modules used in display_data.py"""

import modules

class DisplayData(modules.ModulesPackage):
    """Class that adapts parents modules for DisplayData"""
    class Keyboard(modules.ModulesPackage.Keyboard):
        """Wraps pynput keyboard class and embeds event queue for accesing and organizing key
        events"""
        def consume(self):
            """Iterates through event queue and consumes each key indiviidually"""
            while not self._events.empty():
                event = self._events.get()
                print("{} {}".format(event.get_name(), event.get_key().name))
