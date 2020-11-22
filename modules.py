#!/usr/bin/env python3
"""This script contains all of the modules used in this directory"""

import os
import datetime
import time
import queue
import numpy as np
import cv2
from imutils.video.pivideostream import PiVideoStream
import pynput

KEYBOARD_PRESSED_ITEM_NAME = "pressed"
KEYBOARD_RELEASED_ITEM_NAME = "released"

class ModulesPackage:
    """Contains basic framework of all modules utilized in this directory"""

    @staticmethod
    def check_for_quit_request():
        """Quits if 'q' key is pressed"""
        if cv2.waitKey(1) & 0xFF == ord('q'):
            raise ModulesPackage.Break

    class Break(Exception):
        """Emulates a break from within a function"""

    class DirectoryManagement:
        """Manages the directory and has classes to write and read directories"""
        class WriteDir:
            """Class with methods to add more directories with similar naming conventions"""
            def __init__(self, target_dir, first_dir_name):
                self._target_dir = target_dir
                self._first_dir_name = first_dir_name
                self._names = []
                self._nums = []
                self._most_recent_dir = self._MostRecentDir()
                self._new_folder = None
                os.chdir(target_dir)

            def add(self):
                """Follows naming conventions of the first directory and adds another one"""
                self._names = os.listdir(self.get_target_dir())
                self._nums = []
                self._new_folder = None
                if self._names:
                    self._names = np.sort(self._names)
                    self._nums = []
                    for name in self._names:
                        self._nums = np.append(self._nums, int(''.join(filter(str.isdigit, name))))
                    self._most_recent_dir.calculate(self._names, self._nums)
                    self._new_folder = (self._most_recent_dir.get_text() +
                                        str(self._most_recent_dir.get_num()+1))
                else:
                    self._new_folder = self.get_first_dir_name()
                os.mkdir(self._new_folder)
                os.chdir(self._new_folder)

            def debug(self, debug):
                """Prints out values of all variables for debugging"""
                if debug:
                    print("names: " + str(self._names))
                    print("nums: " + str(self._nums))
                    self._most_recent_dir.debug(True)
                    print("newFolder: " + str(self._new_folder))

            def get_target_dir(self):
                """Returns the directory that this class with manage"""
                return self._target_dir

            def get_first_dir_name(self):
                """Returns the first directory that was made in the target directory"""
                return self._first_dir_name

            class _MostRecentDir:
                def __init__(self):
                    self._index = None
                    self._name = None
                    self._num = None
                    self._text = None

                def calculate(self, names, nums):
                    """Calculates data on the most recent directory from the names and numbers of
                    all of them"""
                    self._num = np.amax(nums)
                    self._index = int(np.where(nums == self._num)[0])
                    self._name = names[self._index]
                    self._num = int(''.join(filter(str.isdigit, self._name)))
                    self._text = ''.join(filter(str.isalpha, self._name))

                def debug(self, debug):
                    """Prints out values of all variables for debugging"""
                    if debug:
                        print("MostRecentDir: index: " + str(self._index))
                        print("MostRecentDir: name: " + str(self._name))
                        print("MostRecentDir: num: " + str(self._num))
                        print("MostRecentDir: text: " + str(self._text))

                def get_index(self):
                    """Returns the index of the most recent directory"""
                    return self._index

                def get_name(self):
                    """Returns the name of the most recent directory"""
                    return self._name

                def get_num(self):
                    """Returns the number of the most recent directory"""
                    return self._num

                def get_text(self):
                    """Returns the text of the most recent directory"""
                    return self._text

        class ReadDir:
            """Class with methods to read and display from an images directory"""
            def __init__(self, target_dir):
                self._target_dir = target_dir
                self._names = []
                self._text = None
                self._ext = None
                self._images = []
                self._img_num = 0
                self._start_delay = None

            def read(self):
                """Cache or Load and Store the images in the target directory"""
                self._names = os.listdir(self.get_target_dir())
                self._text, self._ext = os.path.splitext(self._names[0])
                self._text = ''.join(filter(str.isalpha, self._text))
                for i, name in enumerate(self._names):
                    self._names[i] = int(''.join(filter(str.isdigit, name)))
                self._names.sort()
                self._names = [self._text + str(name) + self._ext for name in self._names]

                self._images = [None for name in self._names]
                for i, name in enumerate(self._names):
                    self._images[i] = cv2.imread(self._target_dir+r'/'+name)
                    self._images[i] = cv2.putText(self._images[i], text=str(i), org=(0, 25),
                                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                                                  color=(0, 255, 0), thickness=2,
                                                  lineType=cv2.LINE_AA)
                self._images = np.array(self._images)

            def imshow(self):
                """Display the image that is next up in the slideshow"""
                if not self._start_delay:
                    cv2.imshow("slideshow", self._images[self._img_num])

            def update(self, delay_ms):
                """Check if delay is completed or if delay needs to be reset"""
                if not self._start_delay:
                    self._img_num += 1
                    if self._img_num >= len(self._images):
                        raise ModulesPackage.Break
                    self._start_delay = datetime.datetime.now()
                elif (datetime.datetime.now() - self._start_delay).total_seconds() >= (delay_ms/1000.0):
                    self._start_delay = None

            def get_target_dir(self):
                """Return name of target directory"""
                return self._target_dir

            def get_names(self):
                """Return image filenames"""
                return self._names

            def get_images(self):
                """Return images in the target directory"""
                return self._images

    class Fps:
        """Computes Fps over a series of frames and their times"""
        def __init__(self):
            self._elapsed_times = np.array([])
            self._ms_to_seconds = 1.0/1000000.0
            self._start_time = None
            self._end_time = None
            self._mean = None
            self._seconds_per_frame = None
            self._fps = None

        def open_timer(self):
            """Starts timer that determines the elapsed time"""
            self._start_time = datetime.datetime.now()

        def close_timer(self):
            """Stops timer that determines the elapsed time"""
            self._end_time = datetime.datetime.now()
            self._elapsed_times = np.append(self._elapsed_times, self._end_time - self._start_time)
            return self._elapsed_times[-1]

        def calculate(self):
            """Calculates the fps based upon a series of stats"""
            self._elapsed_times = np.delete(self._elapsed_times, [0])
            self._mean = np.mean(self._elapsed_times)
            self._seconds_per_frame = self._mean.microseconds * self._ms_to_seconds
            self._fps = 1.0/self._seconds_per_frame

        def print_fps(self):
            """Prints out just fps"""
            print("FPS: " + str(self._fps))

        def debug(self, debug):
            """Prints out values of all variables for debugging"""
            if debug:
                print("startTime: " + str(self._start_time))
                print("endTime: " + str(self._end_time))
                print("elapsedTimes: " + str(self._elapsed_times))
                print("mean: " + str(self._mean))
                print("secondsPerFrame: " + str(self._seconds_per_frame))
                print("fps: " + str(self._fps))

        def get_fps(self):
            """Returns fps"""
            return self._fps

    class Frame:
        """Keeps track of all data regarding the video stream"""
        def __init__(self, name):
            self._width = 640
            self._height = 480
            self._camera = PiVideoStream(resolution=(self._width, self._height)).start()
            time.sleep(2.0)
            self._name = name
            self._frame = None

        def capture_frame(self):
            """Reads the frame from the video stream"""
            self._frame = self._camera.read()

        def preprocessing(self):
            """Preprocesses the frame"""

        def imshow(self):
            """Displays the frame"""
            cv2.imshow(self._name, self._frame)

        def update(self):
            """Checks certain break conditions and updates certain variables"""

        def get_name(self):
            """Returns name of the camera"""
            return self._name

        def get_camera(self):
            """Returns video stream object"""
            return self._camera

        def get_width(self):
            """Returns raw width of frame"""
            return self._width

        def get_height(self):
            """Returns raw height of frame"""
            return self._height

    class Keyboard:
        """Wraps pynput keyboard class and embeds event queue for accesing and organizing key
        events"""
        def __init__(self, len_event_buffers=64):
            self._listener = pynput.keyboard.Listener(on_press=self._on_press,
                                                      on_release=self._on_release)
            self._events = queue.Queue(maxsize=len_event_buffers)

        def _on_press(self, key):
            """Callback for when key is pressed"""
            self._produce(KEYBOARD_PRESSED_ITEM_NAME, key)

        def _on_release(self, key):
            """Callback for when key is released"""
            self._produce(KEYBOARD_RELEASED_ITEM_NAME, key)

        def start(self):
            """Starts listening to the keyboard"""
            self._listener.start()

        def stop(self):
            """Stops listening to the keyboard"""
            self._listener.stop()

        def _produce(self, name, key):
            """Produces key into events queue"""
            self._events.put(self._Item(name, key), block=False)

        def consume(self):
            """Consumes keys in the events queue"""

        def get_events(self):
            """Returns events queue"""
            return self._events

        class _Item:
            def __init__(self, name, key):
                self._name = name
                self._key = key

            def get_name(self):
                """Returns name"""
                return self._name

            def get_key(self):
                """Returns key"""
                return self._key
