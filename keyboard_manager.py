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
        print(self.pressed_movement)
        print(to_press)
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

    def do_wa(self):
        to_press = {'w':True, 'a':True, 's':False, 'd':False}
        self.press_keys(to_press)
        self.pressed_movement = to_press

    def do_a(self):
        to_press = {'w':False, 'a':True, 's':False, 'd':False}
        self.press_keys(to_press)
        self.pressed_movement = to_press

    def do_as(self):
        to_press = {'w':False, 'a':True, 's':True, 'd':False}
        self.press_keys(to_press)
        self.pressed_movement = to_press
    def do_s(self):
        to_press = {'w':False, 'a':False, 's':True, 'd':False}
        self.press_keys(to_press)
        self.pressed_movement = to_press

    def do_sd(self):
        to_press = {'w':False, 'a':False, 's':True, 'd':True}
        self.press_keys(to_press)
        self.pressed_movement = to_press

    def do_d(self):
        to_press = {'w':False, 'a':False, 's':False, 'd':True}
        self.press_keys(to_press)
        self.pressed_movement = to_press

    def do_dw(self):
        to_press = {'w':True, 'a':False, 's':False, 'd':True}
        self.press_keys(to_press)
        self.pressed_movement = to_press



    def do_nothing(self):
        to_press = {'w':False, 'a':False, 's':False, 'd':False}
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