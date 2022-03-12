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

import os
import cv2
import enum
import numpy as np
import pandas as pd
from angle_labeler_utils import AngleLabeler

LABELS_PATH = None
IMAGES_DIR = None
IMAGES_TOTAL_NUM = None
IMAGE_SIZE = None
IMAGE_NAMES = None
SHOW_ANGLE = True
SHOW_NUM = True
ROBOT = None

class State(enum.Enum):
    """Store state of labeler"""
    BROWSE = 0
    EDIT = 1

class Key:
    """Stores important key data"""
    def __init__(self, name, callback):
        self._name = name
        self._callback = callback
        self._state = AngleLabeler.KEYBOARD_RELEASED_STATE
        self._action_type = None
        self._tap_status = None

    def update(self, event):
        """Update data with latest event info"""
        if event.get_name() == self._name:
            self._state = event.get_state()
            self._action_type = event.get_action_type()

    def trigger_callback(self):
        """Update tap status and trigger callback"""
        if self._state == AngleLabeler.KEYBOARD_PRESSED_STATE:
            if self._action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_TAP and not self._tap_status:
                self._callback(self._action_type)
                self._tap_status = True
            elif self._action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_HOLD:
                self._callback(self._action_type)
        elif self._state == AngleLabeler.KEYBOARD_RELEASED_STATE:
            self._tap_status = False

    def set_state(self, new_state):
        """Set state"""
        self._state = new_state

    def set_action_type(self, new_action_type):
        """Set action type"""
        self._action_type = new_action_type

    def set_tap_status(self, new_tap_status):
        """Set status of tap"""
        self._tap_status = new_tap_status

    def get_state(self):
        """Access state"""
        return self._state

    def get_action_type(self):
        """Access action type"""
        return self._action_type

    def get_tap_status(self):
        """Access tap status"""
        return self._tap_status

    def get_name(self):
        """Return key event name"""
        return self._name

image_num = 0
state = State.BROWSE
labels = None
args = None

def compute_angle():
    global image_num, IMAGE_NAMES, labels, ROBOT
    angle = None
    if not ROBOT["y"] - labels.loc[IMAGE_NAMES[image_num], "y"] == 0:
        angle = np.arctan((labels.loc[IMAGE_NAMES[image_num], "x"] - ROBOT["x"])
                          / (ROBOT["y"] - labels.loc[IMAGE_NAMES[image_num], "y"]))
        angle = np.rad2deg(angle)
        angle = round(angle * 100)/100
    else:
        if labels.loc[IMAGE_NAMES[image_num], "x"] - ROBOT["x"] > 0:
            angle = float(90)
        elif labels.loc[IMAGE_NAMES[image_num], "x"] - ROBOT["x"] < 0:
            angle = float(-90)
        else:
            angle = float(0)

    labels.loc[IMAGE_NAMES[image_num], "angle"] = angle

def left_key_callback(action_type):
    """Executes upon press of left key"""
    global image_num, state, IMAGE_NAMES, labels
    if state == State.BROWSE and image_num > 0:
        image_num -= 1
    elif state == State.EDIT and labels.loc[IMAGE_NAMES[image_num], "x"] > 0:
        if action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_HOLD:
            labels.loc[IMAGE_NAMES[image_num], "x"] -= args.sensitivity
        elif action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_TAP:
            labels.loc[IMAGE_NAMES[image_num], "x"] -= 1
        compute_angle()

def right_key_callback(action_type):
    """Executes upon press of right key"""
    global image_num, state, IMAGES_TOTAL_NUM, IMAGE_NAMES, labels
    if state == State.BROWSE and image_num < IMAGES_TOTAL_NUM - 1:
        image_num += 1
    elif state == State.EDIT and labels.loc[IMAGE_NAMES[image_num], "x"] < IMAGE_SIZE - 1:
        if action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_HOLD:
            labels.loc[IMAGE_NAMES[image_num], "x"] += args.sensitivity
        elif action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_TAP:
            labels.loc[IMAGE_NAMES[image_num], "x"] += 1
        compute_angle()

def up_key_callback(action_type):
    """Executes upon press of up key"""
    global image_num, state, IMAGE_NAMES, labels
    if state == State.EDIT and labels.loc[IMAGE_NAMES[image_num], "y"] > 0:
        if action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_HOLD:
            labels.loc[IMAGE_NAMES[image_num], "y"] -= args.sensitivity
        elif action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_TAP:
            labels.loc[IMAGE_NAMES[image_num], "y"] -= 1
        compute_angle()

def down_key_callback(action_type):
    """Executes upon press of down key"""
    global image_num, state, IMAGE_NAMES, labels
    if state == State.EDIT and labels.loc[IMAGE_NAMES[image_num], "y"] < IMAGE_SIZE - 1:
        if action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_HOLD:
            labels.loc[IMAGE_NAMES[image_num], "y"] += args.sensitivity
        elif action_type == AngleLabeler.KEYBOARD_ACTION_TYPE_TAP:
            labels.loc[IMAGE_NAMES[image_num], "y"] += 1
        compute_angle()

def enter_key_callback(_):
    """Executes upon press of enter key"""
    global image_num, state, IMAGE_NAMES, labels
    if state == State.BROWSE:
        state = State.EDIT
        labels.loc[IMAGE_NAMES[image_num], "labeled"] = True
    elif state == State.EDIT:
        state = State.BROWSE
        labels.to_csv(LABELS_PATH)

def backspace_key_callback(_):
    """Executes upon press of backspace key"""
    global image_num, state, IMAGE_NAMES, labels
    if state == State.EDIT:
        state = State.BROWSE
        labels.loc[IMAGE_NAMES[image_num], "angle"] = 0
        labels.loc[IMAGE_NAMES[image_num], "x"] = IMAGE_SIZE // 2
        labels.loc[IMAGE_NAMES[image_num], "y"] = 0
        labels.loc[IMAGE_NAMES[image_num], "labeled"] = False

def shift_key_callback(_):
    """Executes upon press of shift key"""
    global SHOW_ANGLE
    SHOW_ANGLE = not SHOW_ANGLE

def ctrl_key_callback(_):
    """Executes upon press of ctrl key"""
    global SHOW_NUM
    SHOW_NUM = not SHOW_NUM

def main():
    """Main code"""
    global image_num, state, labels, args, LABELS_PATH, IMAGES_DIR, \
           IMAGES_TOTAL_NUM, IMAGE_SIZE, IMAGE_NAMES, SHOW_ANGLE, SHOW_NUM, ROBOT

    AngleLabeler.InitBashArgs()
    args = AngleLabeler.InitBashArgs.get_args()

    LABELS_PATH = args.labels_path
    IMAGES_DIR = args.images_dir

    keyboard = AngleLabeler.Keyboard()
    keyboard.start()

    IMAGE_NAMES = AngleLabeler.Dataset.get_ordered_path(IMAGES_DIR)
    image_file_ext = os.path.splitext(os.listdir(IMAGES_DIR)[0])[1]

    images = {}
    for i, _ in enumerate(IMAGE_NAMES):
        IMAGE_NAMES[i] = os.path.splitext(IMAGE_NAMES[i])[0]
    images[IMAGE_NAMES[image_num]] = cv2.imread(IMAGES_DIR + IMAGE_NAMES[image_num] + image_file_ext)

    IMAGES_TOTAL_NUM = len(IMAGE_NAMES)
    IMAGE_SIZE = images[IMAGE_NAMES[image_num]].shape[0]
    ROBOT = {"x": IMAGE_SIZE//2, "y": IMAGE_SIZE - 1}

    if os.path.isfile(LABELS_PATH):
        labels = pd.read_csv(LABELS_PATH, index_col=0)
        index_list = list(labels.index)
        if index_list != IMAGE_NAMES:
            index_hash = set(index_list)
            new_indices = [name for name in IMAGE_NAMES if name not in index_hash]
            new_labels = pd.DataFrame([0 for i, _ in enumerate(new_indices)], columns=["angle"])
            new_labels = new_labels.assign(x=[IMAGE_SIZE // 2 for i, _ in enumerate(new_indices)])
            new_labels = new_labels.assign(y=[0 for i, _ in enumerate(new_indices)])
            new_labels = new_labels.assign(labeled=[False for i, _ in enumerate(new_indices)])
            new_labels.index = new_indices
            labels = pd.concat([labels, new_labels])
    else:
        labels = pd.DataFrame([0 for i, _ in enumerate(IMAGE_NAMES)], columns=["angle"])
        labels = labels.assign(x=[IMAGE_SIZE // 2 for i, _ in enumerate(IMAGE_NAMES)])
        labels = labels.assign(y=[0 for i, _ in enumerate(IMAGE_NAMES)])
        labels = labels.assign(labeled=[False for i, _ in enumerate(IMAGE_NAMES)])
        labels.index = IMAGE_NAMES

    left_key = Key("left", left_key_callback)
    right_key = Key("right", right_key_callback)
    up_key = Key("up", up_key_callback)
    down_key = Key("down", down_key_callback)
    enter_key = Key("enter", enter_key_callback)
    backspace_key = Key("backspace", backspace_key_callback)
    a_key = Key("a", left_key_callback)
    d_key = Key("d", right_key_callback)
    w_key = Key("w", up_key_callback)
    s_key = Key("s", down_key_callback)
    space_key = Key("space", enter_key_callback)
    e_key = Key("e", backspace_key_callback)
    shift_key = Key("shift", shift_key_callback)
    shift_right_key = Key("shift_r", shift_key_callback)
    ctrl_left_key = Key("ctrl_l", ctrl_key_callback)
    ctrl_right_key = Key("ctrl_r", ctrl_key_callback)

    try:
        while True:
            keyboard.update_events()
            while not keyboard.get_events().empty():
                event = keyboard.get_events().get()
                left_key.update(event)
                right_key.update(event)
                up_key.update(event)
                down_key.update(event)
                enter_key.update(event)
                backspace_key.update(event)
                a_key.update(event)
                d_key.update(event)
                w_key.update(event)
                s_key.update(event)
                space_key.update(event)
                e_key.update(event)
                shift_key.update(event)
                shift_right_key.update(event)
                ctrl_left_key.update(event)
                ctrl_right_key.update(event)

            left_key.trigger_callback()
            right_key.trigger_callback()
            up_key.trigger_callback()
            down_key.trigger_callback()
            enter_key.trigger_callback()
            backspace_key.trigger_callback()
            a_key.trigger_callback()
            d_key.trigger_callback()
            w_key.trigger_callback()
            s_key.trigger_callback()
            space_key.trigger_callback()
            e_key.trigger_callback()
            shift_key.trigger_callback()
            shift_right_key.trigger_callback()
            ctrl_left_key.trigger_callback()
            ctrl_right_key.trigger_callback()

            if not IMAGE_NAMES[image_num] in images:
                images[IMAGE_NAMES[image_num]] = cv2.imread(IMAGES_DIR + IMAGE_NAMES[image_num] + image_file_ext)

            if labels.loc[IMAGE_NAMES[image_num], "labeled"]:
                image_draw = cv2.circle(images[IMAGE_NAMES[image_num]].copy(),
                                        (labels.loc[IMAGE_NAMES[image_num], "x"],
                                        labels.loc[IMAGE_NAMES[image_num], "y"]),
                                        radius=2, color=(0, 255, 0), thickness=-1)
                image_draw = cv2.line(image_draw,
                                    (labels.loc[IMAGE_NAMES[image_num], "x"],
                                    labels.loc[IMAGE_NAMES[image_num], "y"]),
                                    (ROBOT["x"], ROBOT["y"]),
                                    color=(0, 255, 0), thickness=1)

                x_margin = 5
                y_margin = 10
                angle_text_height = 0
                if SHOW_ANGLE:
                    ((width, angle_text_height), baseline) = cv2.getTextSize(text="angle: " + str(labels.loc[IMAGE_NAMES[image_num], "angle"]),
                                                                             fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                                                             fontScale=0.5, thickness=1)

                    image_draw = cv2.putText(image_draw,
                                             text="angle: " + str(labels.loc[IMAGE_NAMES[image_num], "angle"]),
                                             org=(IMAGE_SIZE - width - x_margin, IMAGE_SIZE - angle_text_height + baseline),
                                             fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5,
                                             color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)
                    angle_text_height += y_margin

                if SHOW_NUM:
                    ((width, height), baseline) = cv2.getTextSize(text="image #" + ''.join(filter(str.isdigit, IMAGE_NAMES[image_num])),
                                                                  fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                                                  fontScale=0.4, thickness=1)

                    image_draw = cv2.putText(image_draw,
                                             text="image #" + ''.join(filter(str.isdigit, IMAGE_NAMES[image_num])),
                                             org=(IMAGE_SIZE - width - x_margin, IMAGE_SIZE - height + baseline - angle_text_height),
                                             fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.4,
                                             color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)

                cv2.imshow("image", cv2.resize(image_draw, (IMAGE_SIZE * 2, IMAGE_SIZE * 2)))

            else:
                cv2.imshow("image", cv2.resize(images[IMAGE_NAMES[image_num]],
                                               (IMAGE_SIZE* 2, IMAGE_SIZE* 2)))

            AngleLabeler.check_for_quit_request()

    except AngleLabeler.Break:
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
