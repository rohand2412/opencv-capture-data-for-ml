import os
import cv2
import pickle
import enum
from raspberry_pi_libraries import multi_wrapper

class State(enum.Enum):
    """Store state of labeler"""
    BROWSE = 0
    EDIT = 1

def main():

    state = State.BROWSE

    labels_dir = ""
    images_dir = "/home/rohan/Documents/RCJ2021Repos/raspberry-pi-images-rcj/Evac-Subset-300/Final-Images/"

    keyboard = multi_wrapper.Packages.Keyboard()
    keyboard.start()

    image_names = multi_wrapper.Packages.Dataset.get_ordered_path(images_dir)
    image_file_ext = os.path.splitext(os.listdir(images_dir)[0])[1]

    images = {}
    for i, _ in enumerate(image_names):
        image_names[i] = os.path.splitext(image_names[i])[0]
        images[image_names[i]] = cv2.imread(images_dir + image_names[i] + image_file_ext)

    image_num = 0

    left_key = "left"
    left_key_state = False
    left_key_action_type = None
    left_tap_update = False
    right_key = "right"
    right_key_state = False
    right_key_action_type = None
    right_tap_update = False

    try:
        while True:
            cv2.imshow("image", images[image_names[image_num]])
            while not keyboard.get_events().empty():
                event = keyboard.get_events().get()
                print(event.get_name())
                if event.get_name() == left_key:
                    left_key_state = event.get_state()
                    left_key_action_type = event.get_action_type()
                elif event.get_name() == right_key:
                    right_key_state = event.get_state()
                    right_key_action_type = event.get_action_type()

            if state == State.BROWSE:            
                if left_key_state == multi_wrapper.Packages.KEYBOARD_PRESSED_STATE and image_num > 0:
                    if left_key_action_type == multi_wrapper.Packages.KEYBOARD_ACTION_TYPE_TAP and not left_tap_update:
                        image_num -= 1
                        left_tap_update = True
                    elif left_key_action_type == multi_wrapper.Packages.KEYBOARD_ACTION_TYPE_HOLD:
                        image_num -= 1
                elif left_key_state == multi_wrapper.Packages.KEYBOARD_RELEASED_STATE:
                    left_tap_update = False

                if right_key_state == multi_wrapper.Packages.KEYBOARD_PRESSED_STATE and image_num < (len(images) - 1):
                    if right_key_action_type == multi_wrapper.Packages.KEYBOARD_ACTION_TYPE_TAP and not right_tap_update:
                        image_num += 1
                        right_tap_update = True
                    elif right_key_action_type == multi_wrapper.Packages.KEYBOARD_ACTION_TYPE_HOLD:
                        image_num += 1
                elif right_key_state == multi_wrapper.Packages.KEYBOARD_RELEASED_STATE:
                    right_tap_update = False
            elif state == State.EDIT:
                pass

            multi_wrapper.Packages.check_for_quit_request()

    except multi_wrapper.Packages.Break:
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
