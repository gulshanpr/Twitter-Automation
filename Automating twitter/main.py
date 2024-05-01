import pyautogui
import time

print(pyautogui.size())

pyautogui.moveTo(100,500, duration=2)

pyautogui.moveRel(0,400, duration=1)

print(pyautogui.position())

pyautogui.click(159,702, duration=2)