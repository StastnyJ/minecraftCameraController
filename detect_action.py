from dataclasses import dataclass
import math
from mouse_manager import MouseManager
from keyboard_manager import KeyBoardManager
import numpy as np
import threading
@dataclass
class Hand():
    handedness: str
    gesture: str
    x_coord: float
    y_coord: float


class Gesture_Manager():
    def __init__(self):
        self.mouse_manager = MouseManager()
        self.kbd_mng = KeyBoardManager()
        self.hand_start_pos = None
        self.hold_left_click = False
        self.hold_right_click = False
        self.scrolling = False
        self.mouse_move_thread = None

    def detect_action(self, recognized_gestures):
        
        # While we dont see both hands do nothing
        # if (sorted([handedness[0].category_name for handedness in recognized_gestures.handedness])) != ['Left', 'Right']:
            # return

        # Iterate through hand list and call apropriate resolver functions
        for handedness, gesture, cord_xy in zip(recognized_gestures.handedness, recognized_gestures.gestures, recognized_gestures.hand_landmarks):
            # print(handedness[0].category_name, gesture[0].category_name, cord_xy[0].x, cord_xy[0].y)
            if handedness[0].category_name == 'Left':

                # Load right hand info into our hand data class
                left = Hand(handedness[0].category_name, gesture[0].category_name, cord_xy[0].x, cord_xy[0].y)

                self.handle_left_hand(left)

            # Right hand logic
            if handedness[0].category_name == 'Right':

                # Load right hand info into our hand data class
                right = Hand(handedness[0].category_name, gesture[0].category_name, cord_xy[0].x, cord_xy[0].y)

                self.handle_right_hand(right)

                
    
    def handle_right_hand(self, right):
        """right: right hand object @ hand object"""
        
        # Check if we closed our fist
        if self.hand_start_pos is None and right.gesture == 'Closed_Fist':

            # We releashand_start_pose our left click if its being held
            if self.hold_left_click:
                self.kbd_mng.release_left_click()
                

            # Reset our click booleans 
            self.hold_right_click = False
            self.hold_left_click = False

            # Set starting position for our view move
            self.hand_start_pos = (right.x_coord, right.y_coord)
        
        # Check for view drag release
        if self.hand_start_pos is not None and right.gesture == 'Open_Palm':

            # Create our view drag vector
            vec = (right.x_coord - self.hand_start_pos[0], right.y_coord - self.hand_start_pos[1])
            self.hand_start_pos = None
            print(f"Drag vector: {vec[0]}, {vec[1]}")

            # Keep the gesture loop responsive and avoid overlapping mouse moves.
            if self.mouse_move_thread is None or not self.mouse_move_thread.is_alive():
                self.mouse_move_thread = threading.Thread(
                    target=self.mouse_manager.move_mouse,
                    args=(vec,),
                    daemon=True,
                )
                self.mouse_move_thread.start()

        # Check for left click gesture
        if right.gesture == 'Pointing_Up':
            self.hold_left_click = True
            print("Left click")
            self.kbd_mng.left_click()

        # Check for right click gesture
        if right.gesture == 'Victory':
            self.hold_right_click = True
            print("Right click")
            self.kbd_mng.right_click()
        if right.gesture == 'Thumb_Up' and not self.scrolling:
            print(self.scrolling)
            self.scrolling = True

            print("Scrolling up")
            self.mouse_manager.scroll_up()
        if right.gesture != 'Thumb_Up' and right.gesture != 'Thumb_Down' and self.scrolling:
            print("Stop scrolling")
            self.scrolling = False
        if right.gesture == 'Thumb_Down' and not self.scrolling:
            self.scrolling = True
            self.mouse_manager.scroll_down()
        if right.gesture != 'Thumb_Down' and right.gesture != 'Thumb_Up' and self.scrolling:
            self.scrolling = False
            

    def handle_left_hand(self, left):
        """left: left hand object @ hand object"""
        # this takes care of horizontal movement (eg wasd)
        # to radial coords
        origin = (0.75, 0.5)
        r = np.hypot(left.x_coord - origin[0], left.y_coord - origin[1])
        theta = np.arctan2(left.y_coord - origin[1], left.x_coord - origin[0]) + np.pi
        r2 = 0.5*35/270

        # print(theta/np.pi, r)
 
        if 0 <= r <= 0.5*35/270 and 0<= theta <=2*np.pi:
            self.kbd_mng.do_nothing()
            # print('left hand is in the middle. do nothing')
        elif r < r2:
            self.kbd_mng.do_nothing()
            # print('do nothing; left hand in null sector')
        elif theta < 1/8*np.pi or theta > 15/8*np.pi:
            self.kbd_mng.do_d()
            # print('left hand in sector #1. press D')
        elif 1/8*np.pi < theta < 3/8*np.pi:
            self.kbd_mng.do_dw()
            # print('left hand in sector #2. press WD')
        elif 3/8*np.pi < theta < 5/8*np.pi:
            self.kbd_mng.do_w()
            # print('left hand in sector #3. press W')
        elif 5/8*np.pi < theta < 7/8*np.pi:
            self.kbd_mng.do_wa()
            # print('left hand in sector #4. press WA')
        elif 7/8*np.pi < theta < 9/8*np.pi:
            self.kbd_mng.do_a()
            # print('left hand in sector #5. press A')
        elif 9/8*np.pi < theta < 11/8*np.pi:
            self.kbd_mng.do_as()
            # print('left hand in sector #6. press AS')
        elif 11/8*np.pi < theta < 13/8*np.pi:
            self.kbd_mng.do_s()
            # print('left hand in sector #7. press S')
        elif 13/8*np.pi < theta < 15/8*np.pi:
            self.kbd_mng.do_sd()
            # print('left hand in sector #8. press SD')
        else:
            self.kbd_mng.do_nothing()
            # print('do nothing. left hand is in on the edge of two sectors')

        # this jumps when fist
        if left.gesture == 'Closed_Fist':
            self.kbd_mng.do_space()
        else:
            self.kbd_mng.release_space()

        # opens inventory when love sign
        # if left.gesture == 'ILoveYou':
            # self.kbd_mng.do_e()
        # else:
            # self.kbd_mng.release_e()
            # print('press E to open inventory')
        
        if left.gesture == 'Victory':
            self.kbd_mng.change_inventory_to_right()
        
            # print('move in inventory one to the right')






            
