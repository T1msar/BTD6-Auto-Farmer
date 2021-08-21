from pathlib import Path
import subprocess
import pyautogui
import time

print("MAKE SURE YOU HAVE SPEEDHACK MOD INSTALLED!!!")
print("Starting script in 3 seconds.")
time.sleep(1)
counter = 0
while True:
    if counter == 3:
        break
    counter += 1
    print(f"{counter}")
    time.sleep(1)

cDriveLibrary = "C:/Program Files (x86)/Steam/steamapps/common/BloonsTD6/BloonsTD6.exe"
dDriveLibrary = "D:/SteamLibrary/steamapps/common/BloonsTD6/BloonsTD6.exe"

if Path(cDriveLibrary).is_file():
    print("Found BTD6 Directory!")
    btd6_directory = cDriveLibrary

elif Path(dDriveLibrary).is_file():
    print("Found BTD6 Directory!")
    btd6_directory = dDriveLibrary

else:
    print("Couldn't locate BloonsTD6 directory!")
    btd6_directory = input("Input BTD6 File: ")
    if Path(btd6_directory).is_file():
        print("Found BTD6 Directory!")

subprocess.Popen(btd6_directory)
time.sleep(12.5)

#BTD6 Automatic Map Launch
start_button = None
while start_button == None:
    start_button = pyautogui.locateCenterOnScreen("./resources/start_button.png")
    print("Looking for start button...")

print("Found start button!")
pyautogui.click(start_button)
time.sleep(3)

ok_button = None
while ok_button == None: 
    ok_button = pyautogui.locateCenterOnScreen("./resources/ok_button.png")
    print("Looking for ok button...")

print("Found ok button!")
pyautogui.click(ok_button)
time.sleep(1.5)

pyautogui.click(837, 938)
time.sleep(1.5)

pyautogui.click(1340, 970)
time.sleep(1.5)

pyautogui.click(1641, 422)
time.sleep(1.5)

pyautogui.click(940, 256)
time.sleep(1.5)

pyautogui.click(1277, 421)
time.sleep(1.5)

pyautogui.click(1286, 743)
time.sleep(5)

pyautogui.click(952, 765)
time.sleep(1.5)

# Impoppable strat to win
