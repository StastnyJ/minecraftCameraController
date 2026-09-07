from pymouse import PyMouse

MOUSE_SENSITIVITY = 1

class MouseManager():
    def __init__(self):
        self.mouse = PyMouse()
        pass

    def move_mouse(self, vector):
        """@param vector: [x, y] the vector representing relative movement of the hand
            Moves the mouse by the specified vector
        """

        current_mouse_pos = self.mouse.position()
        self.mouse.move(current_mouse_pos[0] + vector[0] * MOUSE_SENSITIVITY, current_mouse_pos[1] + vector[1] * MOUSE_SENSITIVITY)

    def left_click(self):
        """
        Clicks the left mouse button
        """
        self.mouse.click()

    def right_click(self):
        """
        Clicks the right mouse button
        """
        self.mouse.rightClick()