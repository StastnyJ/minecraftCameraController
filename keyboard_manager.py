from pynput.keyboard import Controller, Key
import time

class KeyBoardManager():

    def __init__(self):
        self.pressed_movement = {'w': False, 'a':False, 's':False, 'd':False}  
        self.pressed_space = False
        self.pressed_e = False
        self.keyboard = Controller()


    def right_click(self):
        pass

    def left_click(self):
        pass

    def release_left_click(self):
        pass

    def press_keys(self, to_press):
        # print(self.pressed_movement)
        # print(to_press)
        for key in 'wasd':
            if self.pressed_movement[key] == to_press[key]:
                continue

            if self.pressed_movement[key] and not to_press[key]:
                self.keyboard.release(key)

            if not self.pressed_movement[key] and to_press[key]:
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

    def do_space(self):
        if not self.pressed_space:
            self.keyboard.press(Key.space)
        self.pressed_space = True

    def release_space(self):
        if self.pressed_space:
            self.keyboard.release(Key.space)
        self.pressed_space = False

    def do_e(self):
        if not self.pressed_e:
            print('do e')
            self.keyboard.press('e')
            self.pressed_e = True

            time.sleep(100/1000)

            print('release e')
            self.keyboard.release('e')
            self.pressed_e = False


    def release_e(self):
        pass
        # if self.pressed_e:

    def change_inventory_to_right(self):
        pass
    



    def clear_all_actions(self):
        self.do_nothing()
        self.release_space()

    def do_nothing(self):
        to_press = {'w':False, 'a':False, 's':False, 'd':False}
        self.press_keys(to_press)
        self.pressed_movement = to_press


    