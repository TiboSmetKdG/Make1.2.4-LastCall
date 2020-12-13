# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Finally, Boss-programming.
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
import PasswordGenerator
import psutil
import socket
import datetime

# CONFIG


# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


# Function that will give you information about your CPU en RAM usage.
def get_system_info():
    cpu_perc = psutil.cpu_percent()                         # Gets CPU usage in percent
    cpu_freq = psutil.cpu_freq(percpu=True)                 # Gets CPU frequency
    ram = psutil.virtual_memory()                           # Get info about RAM
    ram_use = str(round(ram.used / (1024. ** 3), 2))        # Gets used RAM
    ram_tot = str(round(ram.total / (1024. ** 3), 2))       # Gets total RAM

    # Formats the data to a readable string
    sys_info = "\nCPU usage: {}%\nCPU frequency: {}\nRAM usage: {}GB/{}GB".format(cpu_perc, cpu_freq, ram_use, ram_tot)

    return sys_info


# Function that gives you your IP adress
def get_ip_adress():
    ip = socket.gethostbyname(socket.gethostname())         # Gets your IP adress

    # Formats the data to a readable string
    your_ip = "\nYour IP adress is {}".format(ip)

    return your_ip


# Function that gives you a random Password using PasswordGenerator.py
def get_password():
    print("\n")
    PasswordGenerator.main()


# Function that updates your pograms on a Linux System
def get_system_update():
    print("Still needs to be implemented")


# Function that gives you info about today
def get_date_and_time():
    moment = ""

    # Gets the info about today and seperates it in various different variables
    today = datetime.datetime.now()
    weekday = today.strftime("%A")
    day = today.strftime("%d")
    month = today.strftime("%B")
    year = today.strftime("%Y")
    hour = today.strftime("%H")
    minutes = today.strftime("%M")

    # Says a message depending on what time it is.
    if int(hour) < 6:
        moment = "night"
    elif int(hour) < 12:
        moment = "morning"
    elif int(hour) < 18:
        moment = "afternoon"
    elif int(hour) <= 24:
        moment = "evening"

    day_info = "\nIt is {} {} {} {}, it is now {}:{}.\nEnjoy your {}.".format(weekday, day, month, year,
                                                                              hour, minutes, moment)

    return day_info


def main():
    print("Welcome to my pi, what would you like to do?")

    # While loop that will keep the proram running until the user chooses to stop.
    while True:
        # This will print the menu with all the options the user has.
        print("1. System info")
        print("2. IP Adress")
        print("3. Password generator")
        print("4. System Update")
        print("5. Info about today")
        print("6. Exit")

        choice = int(input())

        # Switch that will run the function the user has chosen.
        if choice == 1:
            try:
                print(get_system_info())
                input()
                print("\n\n")
            except NameError:
                print("Something went wrong.")

        elif choice == 2:
            try:
                print(get_ip_adress())
                input()
                print("\n\n")
            except NameError:
                print("Something went wrong.")

        elif choice == 3:
            try:
                get_password()
                input()
                print("\n\n")
            except NameError:
                print("Invalid input.")

        elif choice == 4:
            try:
                get_system_update()
                input()
                print("\n\n")
            except NameError:
                print("Something went wrong.")

        elif choice == 5:
            try:
                print(get_date_and_time())
                input()
                print("\n\n")
            except NameError:
                print("Something went wrong.")

        elif choice == 6:
            exit()


if __name__ == '__main__':
    main()
