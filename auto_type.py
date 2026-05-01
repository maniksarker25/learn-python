import pyautogui
from time import sleep
# pyautogui.write("hello world!",interval=0.25)
# pyautogui.press("enter")

 
sleep(5)
for i in range(0,200):
    pyautogui.write("Message from paython auto script",interval=0.25)
    pyautogui.press("enter")