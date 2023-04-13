# Launcher for an encryption and decryption pyhton files
while True:
    eod = input("\033[1;37mDo you want to \033[0;32m(e)ncrypt \033[1;37mor \033[1;33m(d)ecrypt \033[1;37mtext?")
    if eod == "e":
        with open("Encrypt.py") as f:exec(f.read())
        exit()
    if eod == "d":
        with open("Decrypt.py") as f:exec(f.read())
        exit()
    else:
        print("Please press e for \033[0;32mencrypt \033[1;37mor d for \033[1;33mdecrypt")