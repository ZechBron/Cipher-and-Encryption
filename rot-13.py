#!/bin/python

'''
Cipher: Rot - 13
GitHub: https://github.com/ZechBron/Cipher-and-Encryption

a - n		n - a
b - o		o - b
c - p		p - c
d - q		q - d
e - r		r - e
f - s		s - f
g - t		t - g
h - u		u - h
i - v		v - i
j - w		w - j
k - x		x - k
l - y		y - l
m - z		z - m
'''
print("Cipher: Rot-13\n\n")

def encode(string):
   zCh = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
   encoded = string.translate(zCh)
   print(encoded)

def decode(string):
   ChB = str.maketrans("NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
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

