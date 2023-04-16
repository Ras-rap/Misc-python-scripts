#A simple ascii clock
import time
import os
import art
mode = input("Do you want to have (N)ormal or (B)ig text?")
while True:
    if mode == "N":
        os.system('cls')
        clock = art.text2art(time.strftime('%I:%M:%S'), )
        print(clock)
        time.sleep(1)
    if mode == "B":
        os.system('cls')
        clock = art.text2art(time.strftime('%I:%M:%S'),font = 'doh' )
        print(clock)
        time.sleep(1)
