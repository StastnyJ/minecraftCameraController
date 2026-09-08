from pynput.keyboard import Controller
import time

class KeyBoardManager():

    def __init__(self):
        self.pressed_movement = {'w': False, 'a':False, 's':False, 'd':False}  
        self.pressed_space = False
        self.did_i_pressed_e = False
        self.keyboard = Controller()


    def right_click(self):
        self.keyboard.tap('p')

    def left_click(self):
        self.keyboard.press('o')

    def release_left_click(self):
        self.keyboard.release()

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



    def do_nothing(self):
        to_press = {'w':False, 'a':False, 's':False, 'd':False}
        self.press_keys(to_press)
        self.pressed_movement = to_press


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

    def do_space(self):
        if not self.pressed_space:
            self.keyboard.press(Key.space)
        self.pressed_space = True

    def release_space(self):
        if self.pressed_space:
            self.keyboard.release(Key.space)
        self.pressed_space = False

    def do_e(self):
        if not self.did_i_pressed_e:
            print('do e')
            self.keyboard.press('e')

            time.sleep(100/1000)

            print('release e')
            self.keyboard.release('e')

        self.did_i_pressed_e = True

    def release_e(self):
        if self.did_i_pressed_e:
            self.did_i_pressed_e = False
            print('resetting love gesture')

    def change_inventory_to_right(self):
        pass

    def clear_all_actions(self):
        self.release_space()
        self.do_nothing()
    
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