import pyautogui as gui
import time
c=gui.confirm('Do you want to shut down your computer?','ShutDown Confirmation',buttons=['Yes','No'])
if c=='Yes':
    ch=gui.confirm('Is your internet ON?','Internet Status',buttons=['Yes','No'])
    if ch=='Yes':
        gui.keyDown('win')
        time.sleep(0.5)
        gui.press('a')
        time.sleep(0.5)
        gui.keyUp('win')
        time.sleep(0.5)
        gui.press('enter')
        time.sleep(0.5)
    gui.press('win')
    time.sleep(0.5)
    gui.press('up')
    time.sleep(0.5)
    gui.press('right')
    time.sleep(0.5)
    gui.press('enter')
    time.sleep(0.5)
    gui.press('down')
    time.sleep(0.5)
    gui.press('down')
    time.sleep(0.5)
    gui.press('enter')
else:
    pass
