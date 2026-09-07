from dataclasses import dataclass

@dataclass
class Hand():
    handedness: str
    gesture: str
    x_coord: float
    y_coord: float

hand_start_pos = None
def detect_action(recognized_gestures):
    if (sorted([handedness[0].category_name for handedness in recognized_gestures.handedness])) != ['Left', 'Right']:
        return

    for handedness, gesture, cord_xy in zip(recognized_gestures.handedness, recognized_gestures.gestures, recognized_gestures.hand_landmarks):
        # print(handedness[0].category_name, gesture[0].category_name, cord_xy[0].x, cord_xy[0].y)
        if handedness[0].category_name == 'Left':
            left = Hand(handedness[0].category_name, gesture[0].category_name, cord_xy[0].x, cord_xy[0].y)
        if handedness[0].category_name == 'Right':
            right = Hand(handedness[0].category_name, gesture[0].category_name, cord_xy[0].x, cord_xy[0].y)



        
