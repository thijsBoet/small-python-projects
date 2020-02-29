import time
import os
from playsound import playsound

os.chdir('D:\\python\\small-python-projects\\break-timer')
minutes = int(input('Set minutes for break timer: '))

def breakTimer(minutes):
    convertSecToMinutes = minutes * 60
    time.sleep(convertSecToMinutes)
    print('Time for a break!')
    playsound('churchBell.wav')

breakTimer(minutes)