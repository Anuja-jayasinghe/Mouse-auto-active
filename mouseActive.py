import pyautogui as anuja
import random
import time

while True:
    x = random.randint(1600,1700)
    y = random.randint(200,600)
    anuja.moveTo(x,y,0.5)
    time.sleep(3)