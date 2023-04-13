#Guess the number game
import random
import os
os.system("cls")
trys = 0
#Ask the user if they want easy, medium, or hard mode
print("\033[1;37m Welcome to the Guess the Number Game!")
voice = input("\033[1;37m Do you want the game to speak? ")
if voice == "yes":
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say("Do you want easy, medium, or hard mode")
        engine.runAndWait()
        mode = input("\033[1;37m Do you want \033[0;32measy\033[1;37m, \033[1;33mmedium\033[1;37m, or \033[0;31mhard \033[1;37mmode? ")
    except:
        print("\033[1;37m You do not have the pyttsx3 module installed")
        Warning = input("\033[1;37m Do you want to install it? ")
        if Warning == "yes":
            os.system("pip install pyttsx3")
            os.system("cls")
            print("\033[1;37m You have installed the pyttsx3 module")
            print("\033[1;37m Please restart the game")
            exit()
        if Warning == "no":
            print("\033[1;37m You have not installed the pyttsx3 module")
            print("\033[1;37m Please install it")
            exit()
else:
    mode = input("\033[1;37m Do you want \033[0;32measy\033[1;37m, \033[1;33mmedium\033[1;37m, or \033[0;31mhard \033[1;37mmode? ")

if mode == "easy":
    print("\033[1;37m You have chosen \033[0;32measy mode")
    print("\033[1;37m The number is between 1 and 100")
    if voice == "yes":
        engine.say("You have chosen easy mode")
        engine.say("The number is between 1 and 100")
        engine.runAndWait()
    number = random.randint(1, 100)
if mode == "medium":
    print("\033[1;37m You have chosen \033[1;33mmedium mode")
    print("\033[1;37m The number is between 1 and 500")
    if voice == "yes":
        engine.say("You have chosen medium mode")
        engine.say("The number is between 1 and 500")
        engine.runAndWait()
    number = random.randint(1, 500)
if mode == "hard":
    print("\033[1;37m You have chosen \033[0;31mhard mode")
    print("\033[1;37m The number is between 1 and 1000")
    if voice == "yes":
        engine.say("You have chosen hard mode")
        engine.say("The number is between 1 and 1000")
        engine.runAndWait()
    number = random.randint(1, 1000)
while True:
#Ask the user to guess the number
    
    if voice == "yes":
        engine.say("Guess the number")
        engine.runAndWait()
        guess = int(input("\033[1;37m Guess the number: "))
        guess = int(guess)
    else:
        guess = int(input("\033[1;37m Guess the number: "))
        guess = int(guess)
#Check if the guess is correct
    if guess == number:
        print("\033[1;37m You guessed the number!")
        print("\033[1;37m You win!")
        print('\033[1;37m You guessed the number in',trys,'trys')
        if voice == "yes":
            engine.say("You guessed the number")
            engine.say("You win")
            engine.runAndWait()
        break
#Check if the guess is too high
    if guess > number:
        print("\033[1;37m You guessed too high!")
        print("\033[1;37m Try again!")
        trys += 1
        if voice == "yes":
            engine.say("You guessed too high")
            engine.say("Try again")
            engine.runAndWait()
#Check if the guess is too low
    if guess < number:
        print("\033[1;37m You guessed too low!")
        print("\033[1;37m Try again!")
        trys += 1
        if voice == "yes":
            engine.say("You guessed too low")
            engine.say("Try again")
            engine.runAndWait()
        