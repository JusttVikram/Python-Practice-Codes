import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    for i in range (0,100):
        pyautogui.moveTo(1000, 1*10)
    time.sleep(5)