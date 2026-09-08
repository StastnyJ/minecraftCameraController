from pynput.keyboard import Controller
import time

keyboard = Controller()

print("Switch to Minecraft...")
time.sleep(2)

print("opening inventory")

keyboard.tap('e')
# keyboard.type('e')

print("Stopped")