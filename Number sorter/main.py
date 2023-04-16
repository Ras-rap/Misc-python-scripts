#A number sorter
import art
import os
import time
from art import aprint

print(art.text2art("Number Sorter"))
time.sleep(1)
os.system("cls")


numbers = []

numbers = [int(item) for item in input("Enter the numbers to be sorted : ").split()]

numbers.sort()
#Loading animation
os.system("cls")
print("Loaded 0%")
aprint("loading1")
time.sleep(0.5)
os.system("cls")
print("Loaded 20%")
aprint("loading2")
time.sleep(0.5)
os.system("cls")
print("Loaded 40%")
aprint("loading3")
time.sleep(0.5)
os.system("cls")
print("Loaded 60%")
aprint("loading4")
time.sleep(0.5)
os.system("cls")
print("Loaded 80%")
aprint("loading5")
time.sleep(0.5)
os.system("cls")
print("Loaded 100%")
aprint("loading6")
time.sleep(0.5)
os.system("cls")

print("Sorted list of numbers : ", numbers)