
import math
import pyautogui

r = 200
xc = 500
yc = 500
alpha = 0

pyautogui.PAUSE = 0.00

while True:
    x = int(r * math.cos(alpha)) + xc
    y = int(r * math.sin(alpha)) + yc
    alpha = alpha + 0.001
    pyautogui.moveTo(x, y, duration=0)