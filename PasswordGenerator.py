# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　A python script that will generate a random password.
　　　　　　  ＼＿＿　＿＿＿＿＿＿＿
　　　　　　　　　  ∨
            ██████████  ████
        ████▒▒░░░░░░░░██▒▒░░██
      ██▒▒░░░░██░░██░░░░██░░░░██
    ██▒▒░░░░░░██░░██░░░░░░▒▒░░██
    ██░░░░░░░░██░░██░░░░░░▒▒▒▒██
  ██░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒██
██▒▒░░░░░░░░░░░░██░░░░░░░░░░░░██
██░░░░▒▒░░░░░░░░██░░░░░░░░░░▒▒██
██░░░░▒▒░░░░░░░░░░░░░░░░░░░░██  
  ██████░░░░░░░░░░░░░░░░░░▒▒██  
██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░▒▒██  
██▒▒▒▒▒▒▒▒██░░░░░░░░░░░░▒▒██    
██▒▒▒▒▒▒▒▒██░░░░░░░░░░▒▒████    
  ██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒████▒▒▒▒██  
    ██▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒██
      ██████      ████████████  
"""

# IMPORTS
import string
import random

# CONFIG
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = string.digits
PUNCTUATION = string.punctuation


# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


def generate_password(leng, get, up, low, spec):
    ww = ""

    character_list = [UPPERCASE, LOWERCASE, NUMBERS, PUNCTUATION]

    # Checks the choises of the user and adds characters when needed
    if get:
        ww = ww + character_list[0][random.randint(0, len(NUMBERS) - 1)]
    if up:
        ww = ww + character_list[0][random.randint(0, len(UPPERCASE) - 1)]
    if low:
        ww = ww + character_list[0][random.randint(0, len(UPPERCASE) - 1)]
    if spec:
        ww = ww + character_list[0][random.randint(0, len(PUNCTUATION) - 1)]

    # this will add characters until the desired length is reached
    i = 0
    while i < leng - len(ww):
        index = random.randint(0, 3)
        ww = ww + character_list[index][random.randint(0, len(character_list[index]) - 1)]
    return ww


def main():
    print("Password generator:")

    # Asks the user what characters they need in their password
    print("How long should your password be?")
    length = int(input())

    print("Should it contail numbers? (yes = 1 / no = 0)")
    num = bool(input())

    print("Should it contail upper case letters? (yes = 1 / no = 0)")
    upper = bool(input())

    print("Should it contail lower case letters? (yes = 1 / no = 0)")
    lower = bool(input())

    print("Should it contail special characters? (yes = 1 / no = 0)")
    spec = bool(input())

    password = generate_password(length, num, upper, lower, spec)
    print("Your password is:", password)


if __name__ == '__main__':
    main()
