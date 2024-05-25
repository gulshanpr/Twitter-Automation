import pyautogui
import time

time.sleep(4)

# This only works on firfox with 100% view
# and the screen size should be 1920 x 1080


# This is for creating new tab (after some time i will make it a combination of hotkey instead of moving and clicking)
# pyautogui.moveTo(1564,32,duration=2)
# pyautogui.click()

# This does above task of opening a new tab
pyautogui.hotkey("ctrl", "t")

# This code will take me to twitter
pyautogui.moveTo(405,96,duration=1)
pyautogui.click()
with open('openingTabURL.txt', 'r') as x:
    URL = x.read()
pyautogui.typewrite(URL)
pyautogui.moveTo(1419,97,duration=1)
pyautogui.click()
time.sleep(3)

# This will write the post
pyautogui.moveTo(577,339,duration=1)
pyautogui.click()
with open('tweetContent.txt', 'r') as x:
    tweetContent = x.read()
pyautogui.typewrite(tweetContent)

# This will post on twitter
pyautogui.moveTo(1257,540,duration=1)
pyautogui.click()
# samyak saying hii and testing he's PR
