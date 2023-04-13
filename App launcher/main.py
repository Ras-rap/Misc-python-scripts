#An app laucncher for all my python scripts i make
import os
os.system("cls")
print("Welcome to the app launcher")
print("1. Guess the number")
print("2. Message encrypter")
print("3. Message decrypter")
print("4. Ghost text")
print("5. Calculator")
print("6. Quit")

appnum = input("Please type the number of the app you want to launch: ")
if appnum == "1":
    with open("Gtn.py") as f:exec(f.read())
if appnum == "2":
    with open("Encrypt.py") as f:exec(f.read())
if appnum == "3":
    with open("Decrypt.py") as f:exec(f.read())
if appnum == "4":
    with open("Ghost.py") as f:exec(f.read())
if appnum == "5":
    with open("Calc.py") as f:exec(f.read())
if appnum == "6":
    exit()