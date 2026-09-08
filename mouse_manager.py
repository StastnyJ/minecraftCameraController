import pyautogui
import time
import math

MOUSE_SENSITIVITY = 3000

class MouseManager():
    def __init__(self):
        pass

    def move_mouse(self, vector):
        """@param vector: [x, y] the vector representing relative movement of the hand
            Moves the mouse by the specified vector
        """

        
        current_mouse_pos = pyautogui.position()
        print(current_mouse_pos)
        new_pos = (math.floor(current_mouse_pos.x + vector[0] * MOUSE_SENSITIVITY), math.floor(current_mouse_pos.y + vector[1] * MOUSE_SENSITIVITY))
        print(new_pos)
        pyautogui.moveTo(new_pos)
        print(f"Moved mouse to {pyautogui.position()}")

    def scroll_down(self):
        pyautogui.scroll(1)

    def scroll_up(self):
        pyautogui.scroll(-1)