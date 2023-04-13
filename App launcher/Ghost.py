import time
import random
import pyttsx3
engine = pyttsx3.init()
spooks = [' Die', ' Left', ' Right', ' Enemy', ' Friend', ' Brynlee', ' Nate', ' Matilda', ' Sit', ' Oww', ' Murdered', ' Hung', ' Gay',
           ' Lesbian', ' Trans', ' Josh', ' Playstation', ]
times = [5, 6, 7, 8, 9, 10, 11]
print("\033[1;37m Starting ghost scanner")
time.sleep(2)
print("\033[1;32m Camera found")
time.sleep(2)
print("\033[1;32m GPS found")
time.sleep(2)
print("\033[0;31m Electromagnetic field detector not found")
time.sleep(2)
input("\033[1;37m Please calibrate")
print("\033[1;37m Calibrated")
while True:
 time.sleep(random.choice(times))
 spook = random.choice(spooks)
 print(spook)
 engine.say(spook)
 engine.runAndWait()