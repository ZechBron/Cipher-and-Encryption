#!/bin/python

'''
Cipher: Qwerty Abcde
Coded By: Zech Bron
Description:
   I've created Qwerty Abcde which is based from keyboard.
'''
print("Cipher: Qwerty ~ Abcdef")
print("Description: Qwerty Abcdef based from keyboard.\n Where Q is A, W is B ... and M is Z\n\n")


def encode(string):
   zCh = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
   encoded = string.translate(zCh)
   print(encoded)

def decode(string):
   ChB = str.maketrans("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
   decoded = string.translate(ChB)
   print(decoded)

print("\033[1;32mWhat do you want to do?\033[0;0m")
print("\033[1;36m a. Encode")
print(" b. Decode\033[0;0m")
zch = input("\033[1;34m[\033[0;0m\033[1;31mZ\033[0;0m\033[1;34m]\033[0;0m \033[1;32mPlease Choose: \033[0;m\033[1;34m")
if zch == 'A' or zch == 'a':
   zech = input("\033[1;34m[\033[0;0m\033[1;31mZ\033[0;0m\033[1;34m]\033[0;0m \033[1;32mEnter text to encode: \033[0;0m\033[1;34m")
   print("\033[0;0m\033[1;34m[\033[0;0m\033[1;31mZ\033[0;0m\033[1;34m]\033[0;0m \033[1;32mEncoded Text: \033[0;0m\033[1;36m")
   encode(zech)

elif zch == 'B' or zch == 'b':
   zech = input("\033[1;34m[\033[0;0m\033[1;31mZ\033[0;0m\033[1;34m]\033[0;0m \033[1;32mEnter text to decode: \033[0;0m\033[1;34m")
   print("\033[0;0m\033[1;34m[\033[0;0m\033[1;31mZ\033[0;0m\033[1;34m]\033[0;0m \033[1;32mDecoded Text: \033[0;0m\033[1;36m")
   decode(zech)

else:
   print("\033[1;31mWrong input. Try again. \033[0;0m")

