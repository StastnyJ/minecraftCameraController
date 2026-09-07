from dataclasses import dataclass
import math
from mouse_manager import MouseManager
import numpy as np
@dataclass
class Hand():
    handedness: str
    gesture: str
    x_coord: float
    y_coord: float







class Gesture_Manager():
    def __init__(self):
        self.mouse_manager = MouseManager()
        self.hand_start_pos = None
        self.hold_left_click = False
        self.hold_right_click = False

    def detect_action(self, recognized_gestures):
        if (sorted([handedness[0].category_name for handedness in recognized_gestures.handedness])) != ['Left', 'Right']:
            return
        for handedness, gesture, cord_xy in zip(recognized_gestures.handedness, recognized_gestures.gestures, recognized_gestures.hand_landmarks):
            # print(handedness[0].category_name, gesture[0].category_name, cord_xy[0].x, cord_xy[0].y)
            if handedness[0].category_name == 'Left':
                left = Hand(handedness[0].category_name, gesture[0].category_name, cord_xy[0].x, cord_xy[0].y)
                self.handle_left_hand(left)

            if handedness[0].category_name == 'Right':
                right = Hand(handedness[0].category_name, gesture[0].category_name, cord_xy[0].x, cord_xy[0].y)
                if self.hand_start_pos is None and right.gesture == 'Closed_Fist':
                    if self.hold_left_click or self.hold_right_click:
                        print("Release click")
                    self.hold_right_click = False
                    self.hold_left_click = False
                    self.hand_start_pos = (right.x_coord, right.y_coord)
                if self.hand_start_pos is not None and right.gesture == 'Open_Fist':
                    vec = (right.x_coord - self.hand_start_pos[0], right.y_coord - self.hand_start_pos[1])
                    self.hand_start_pos = None
                    print(*vec)
                    self.mouse_manager.move_mouse(vec)
                if right.gesture == 'Pointing_Up':
                    self.hold_left_click = True
                    print("Left click")
                    self.mouse_manager.left_click()
                if right.gesture == 'Victory':
                    self.hold_right_click = True
                    print("Right click")
                    self.mouse_manager.right_click()
            

    def handle_left_hand(self, left):
        """left: left hand object @ hand object"""
        # this takes care of horizontal movement (eg wasd)
        # to radial coords
        origin = (0.25, 0.5)
        r = np.hypot(left.x_cord - origin[0], left.y_cord - origin[1])
        theta = np.arctan2(left.y_cord - origin[1], left.x_cord - origin[0])
        r2 = 0.5*101/270
        if 0 <= r <= 0.5*67/270 and 0<= theta <=2*np.pi:
            print('left hand is in the middle. do nothing')
        elif r < r2:
            print('do nothing; left hand in null sector')
        elif theta < 1/8*np.pi or theta > 15/8*np.pi:
            print('left hand in sector #1. press D')
        elif 1/8*np.pi < theta < 3/8*np.pi:
            print('left hand in sector #2. press WD')
        elif 3/8*np.pi < theta < 5/8*np.pi:
            print('left hand in sector #3. press W')
        elif 5/8*np.pi < theta < 7/8*np.pi:
            print('left hand in sector #4. press WA')
        elif 7/8*np.pi < theta < 9/8*np.pi:
            print('left hand in sector #5. press A')
        elif 9/8*np.pi < theta < 11/8*np.pi:
            print('left hand in sector #6. press AS')
        elif 11/8*np.pi < theta < 13/8*np.pi:
            print('left hand in sector #7. press S')
        elif 13/8*np.pi < theta < 15/8*np.pi:
            print('left hand in sector #8. press SD')
        else:
            print('do nothing. left hand is in on the edge of two sectors')

        # this jumps when fist
        if left.gesture == 'Closed_Fist':
            print('press SPACE for jump')

        # opens inventory when love sign
        elif left.gesture == 'Love':
            print('press E to open inventory')
        
        elif left.gesture == 'Victory':
            print('move in inventory one to the right')





            
