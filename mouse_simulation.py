import pyautogui

y = 680
i = 0
for x in range(465, 1532, 1): # 起始位置的x坐标为2400，长度为1020水平方向上的位移（步长设为1）
    pyautogui.moveTo(x, y, duration=0.1)
    i += 1
    # region参数，截图区域，由左上角坐标、宽度、高度4个值确定，如果指定区域超出了屏幕范围，超出部分会被黑色填充，默认`None`，截全屏
    pyautogui.screenshot('D:/FYJ/Choice大数据/second_daily_screenshots/second_daily_shot{}.png'.format(i), region=(450, 310, 1100, 350))


