import time

import pyautogui

pyautogui.click(550, 190)
for i in range(4630, 4650):
    time.sleep(1)
    pyautogui.click(550, 305)
    time.sleep(1.0)
    pyautogui.hotkey('ctrl','a')           #按键ctrl+a
    time.sleep(0.5)
    pyautogui.click(420, 90)
    time.sleep(0.5)
    pyautogui.typewrite("{}-timeseries-20210330.xls".format(i))       #输入文件名，每次跑程序前要完成输入法中英文切换
    time.sleep(1)
    pyautogui.hotkey('enter')           #按键enter
    time.sleep(1)
    pyautogui.click(550, 190)
    time.sleep(1)
    pyautogui.hotkey('down')           #按下方向键
