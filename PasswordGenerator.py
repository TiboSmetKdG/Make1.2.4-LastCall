# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Een python script dat random wachtwoorden genereert.
　　　　　　  |　  - zowel kleine letters als grote, cijfers en tekens
　　　　　　  |　  - op aanvraag de complexiteit (aantal tekens en soort tekens)
　　　　　　  |　  - maak gebruik van flowcontrol en functies!
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

    if get:
        ww = ww + character_list[0][random.randint(0, len(NUMBERS) - 1)]
    if up:
        ww = ww + character_list[0][random.randint(0, len(UPPERCASE) - 1)]
    if low:
        ww = ww + character_list[0][random.randint(0, len(UPPERCASE) - 1)]
    if spec:
        ww = ww + character_list[0][random.randint(0, len(PUNCTUATION) - 1)]

    i = 0
    while i < leng - len(ww):
        index = random.randint(0, 3)
        ww = ww + character_list[index][random.randint(0, len(character_list[index]) - 1)]
    return ww


def main():
    print("Wachtwoord generator:")

    print("Hoe lang moet het wachtwoord zijn?")
    lengte = int(input())

    print("Moet het wachtwoord getallen bevatten? (0 = neen / 1 = ja) ")
    getal = bool(input())

    print("Moet het wachtwoord hoofdletters bevatten? (0 = neen / 1 = ja) ")
    upper = bool(input())

    print("Moet het wachtwoord kleine letters bevatten? (0 = neen / 1 = ja) ")
    lower = bool(input())

    print("Moet het wachtwoord speciale tekens bevatten? (0 = neen / 1 = ja) ")
    specials = bool(input())

    wachtwoord = generate_password(lengte, getal, upper, lower, specials)
    print("Je wachtwoord is:", wachtwoord)


if __name__ == '__main__':
    main()
