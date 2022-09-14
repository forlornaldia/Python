from time import sleep
import pyautogui

mouse_x = 700
mouse_y = 700

def noyell():
    pyautogui.moveTo(mouse_x, mouse_y, .5)
    sleep(.5)
    pyautogui.moveTo(mouse_x+100, mouse_y-100, .5)
    sleep(6)
    noyell()

noyell()