import ctypes
import time
import sys
print("Do you want to continue")
continuing =input()
#
while continuing == "yes":
    time.sleep(1)
    ctypes.windll.user32.LockWorkStation()
    time.sleep(10)
if continuing == "no":
    exit()

