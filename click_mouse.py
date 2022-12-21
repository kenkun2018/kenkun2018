import pyautogui
import time

# pyautogui.FAILSAFE = True

width, height = pyautogui.size()

def click():
    sleeptime = 10
    # print (m, n)
    pyautogui.moveTo(width/2, height/2, duration=2)
    while True:
        pyautogui.moveTo(width/2, height/2 - 200, duration=2)
        pyautogui.click()
        time.sleep(sleeptime)

        pyautogui.moveTo(width / 2, height / 2, duration=2)
        pyautogui.click()
        time.sleep(sleeptime)

if __name__ == '__main__':
    click()