import mouse
import keyboard
import time

while True:
    if keyboard.is_pressed("m"):
        mouse.click("left")
        time.sleep(0.02)