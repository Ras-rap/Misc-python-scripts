# Description: Encrypts a message using Base64 and a ceaser cipher
#Made by Ras_rap#2027
import base64

#Define the function to be used in the ceaser cipher
def ceasar(story, shift):
  return ''.join([ # concentrate list to string
            (lambda c, is_upper: c.upper() if is_upper else c) # if original char is upper case than convert result to upper case too
                (
                  ("abcdefghijklmnopqrstuvwxyz"*2)[ord(char.lower()) - ord('a') + shift % 26], # rotate char, this is extra easy since Python accepts list indexs below 0
                  char.isupper()
                )
            if char.isalpha() else char # if not in alphabet then don't change it
            for char in story 
        ])

#Ask the user for the message to be encrypted and encodes it to base64  
string = input("\033[1;37mEnter the content of the message to be encrypted: ")
shift = int(input("\033[1;37mEnter the number to be used in the ceaser cipher: "))
string = string.encode("ascii")
print (f"\033[1;37mNumber: \033[0;31m{shift}")

#Encodes the given sentence into base64 
base64_bytes = base64.b64encode(string)
base64_string = base64_bytes.decode("ascii")
cshift = ceasar(base64_string,shift)

#Asks the user for the number to be used in the ceaser cipher and ciphers the base64 message



print(f"\033[1;37mEncryted message: \033[0;32m{cshift}\033[1;37m")