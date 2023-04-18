#A installer for a discord webhook spammer.
#By: Ras_rap#2027
#Version: 1.0.0
#Date: 11/10/2021
import os
try:
    from discordwebhook import Discord
    with open("Spammer.py") as f:exec(f.read())
except:
    print("You do not have Discordwebhook installed.")
    download = input("Would you like to download it now? (y/n) or e to try to run it without it: ")
    if download == "y":
        os.system("pip install discord-webhook")
    if download == "n":
        print("This script requires discordwebhook to work. Please install it and try again.")
        exit()
    if download == "e":
        confirm = input("Are you sure you want to run this script without it? (y/n): ")
        if confirm == "y":
            with open("Spammer.py") as f:exec(f.read())
            exit()
        if confirm == "n":
            print("Exiting...")
            exit()
        else:
            print("Invalid input.")
            exit()
    else:
        print("Invalid input.")
        exit()
