# Description: Decrypts a message using Base64 and a ceaser cipher
#Made by Ras_rap#2027
import base64
# Define the characters to be used in the ceaser cipher  
upper = {ascii:chr(ascii) for ascii in range(65,91)}
lower = {ascii:chr(ascii) for ascii in range(97,123)}
digit = {ascii:chr(ascii) for ascii in range(48,58)}

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
#Asks the user what the shift and encrypted message are
string = input("\033[1;37mEnter the content of the message to be decrypted: ")
shift = int(input("\033[1;37mEnter the number to be used in the ceaser cipher: "))  
unshift = -shift
cshift = ceasar(string,unshift)

#Prints the shift number and uhhhh idk
string = string.encode("ascii")
print (f"\033[1;37mNumber: \033[0;31m{shift}")

#Unencodes the base64 message
base64_bytes = base64.b64decode(cshift)
base64_string = base64_bytes.decode("ascii")

#Prints the unencrypted message 
print(f"\033[1;37mUnencrypted message: \033[0;32m{base64_string}\033[1;37m")