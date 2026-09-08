from pynput.keyboard import Controller
import time

keyboard = Controller()

print("Switch to Minecraft...")
time.sleep(5)

print("Walking forward")
keyboard.press('w')

time.sleep(10)
keyboard.release('w')

print("Stopped")