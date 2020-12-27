
import pyautogui
import time

pyautogui.FAILSAFE = False

timePeriod = int(input("Stay awake for (in minutes): "))
runFor = (timePeriod / 3)

i = 0
while i < runFor:
    pauseDuration = (3 * 60) #in seconds
    time.sleep(pauseDuration)

    for move in range(0, 100):
        moveFrom = 0
        moveUpto = move*5
        pyautogui.moveTo(moveFrom, moveUpto)

    i += 1
    print("Running for " + str(i * (3 + 10.84/60)) + " minutes till now")
print("Program terminated")