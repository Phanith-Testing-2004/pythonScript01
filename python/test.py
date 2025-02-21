import pyautogui
import time

msg = input("Input message for lung your ss: ")
n = int(input("Input number for lung your ss: "))

time.sleep(3)

for i in range(n):
    pyautogui.typewrite(msg + " " + str(i + 1))
    pyautogui.typewrite(['enter'])
    time.sleep(0.5)
