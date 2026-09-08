from pynput.keyboard import Controller
import time

class KeyBoardManager():

    def __init__(self):
        self.pressed_movement = {'w': False, 'a':False, 's':False, 'd':False}  
        self.keyboard = Controller()


    def right_click(self):
        pass

    def left_click(self):
        pass

    def release_left_click(self):
        pass

    def press_keys(self, to_press):
        for key in 'wasd':
            if self.pressed_movement[key] == to_press[key]:
                continue

            if self.pressed_movement[key] and not to_press[key]:
                print('release W')
                self.keyboard.release(key)

            if not self.pressed_movement[key] and to_press[key]:
                print('press W')
                self.keyboard.press(key)




    def do_w(self):
        to_press = {'w':True, 'a':False, 's':False, 'd':False}
        self.press_keys(to_press)
        self.pressed_movement = to_press
    
"""

import time


print("Switch to Minecraft...")
time.sleep(5)

print("Walking forward")
keyboard.press('w')

time.sleep(10)
keyboard.release('w')

print("Stopped")
"""