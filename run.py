import time
import random
import os
import textwrap
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('score_board')

# Colors

i_color = Fore.WHITE        # Input Color
c_color = Fore.GREEN        # Correct Answer Color
w_color = Fore.RED          # Wrong Answer Color
h_color = Fore.CYAN         # Hint Color
e_color = Back.RED          # Error Message Color
reset_all = Style.RESET_ALL  # Reset to normal


def clear_board():
    '''
    Clears the terminal when needed
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_message():
    '''
    Display the welcome logo and message
    '''
    print(Style.BRIGHT + Fore.BLUE + Back.WHITE + r'''
    ___           _                _        __ _         ___         _     
    / __| _ __ __ (_) _ __   _ __  (_) _ _  / _` |       / _ \  _  _ (_) ___
    \__ \ \ V  V /| || '  \ | '  \ | || ' \ \__. |      | (_) || || || ||_ /
    |___/  \_/\_/ |_||_|_|_||_|_|_||_||_||_||___/        \__\_\ \_._||_|/__|
    ''' + Style.RESET_ALL)
    time.sleep(3)

    print()

    print(Style.BRIGHT + Fore.BLUE + Back.WHITE + r'''
        .-;'`  `'-.
    /   \       `\_..
    |-"``;-.      || `\
    \    '.`-.   /|  /
        `-.   '. \  |-'`
        `-.  ) \ |
            /` /  / |
        / /`   | |
        / (     ) /
        _(   `-,-'_/
    /  `""""";`
    `---..---'
        //\\
        //---0
    _//_____
    jgs        `\
                (~^~_-~^-~^_~^~^-~^_~-^~_^~-^-~^~^_~^~-^~^~^~-^~_
                ''' + Style.RESET_ALL)
    time.sleep(3)

    print()

    print(Style.RESET_ALL + 'Welcome to the swimming quiz!\n')
    print('Are you ready to test you knowledge about swimming?\n')
    input("Press Enter to continue...")


def menu():
    '''
    A menu with three options for the player to choose from
    '''
    print("[1] Rules")
    print("[2] Play")
    print("[0] Quit")


menu()
option = int(input("Enter your option here: "))

while True:
    try:
        option = int(input("Enter your option here: "))
        if option not in [1, 2, 0]:
            raise ValueError("Invalid Option! Enter: 1, 2, or 0")
        if option == 1:
            rules = [
                "The player is presented with a question and possible answers",
                "The player answers by entering the correct letter.",
                "If the player selects the correct answer, they earn a point.",
                "If the answer is incorrect, no points are earned.",
                "The game proceeds with new questions until all are answered.",
                "At the end of the game, the player's score is displayed."
            ]
            for rule in rules:
                for line in textwrap.wrap(rule, width=79):
                    print(line)
                time.sleep(2)
        elif option == 2:
            print("Play")
        else:
            print("Thank you for playing. See you soon!")
            break
    except ValueError as e:
        print(e)


def main_functions():
    '''
    Calls the main functions on the terminal
    '''
    clear_board()
    welcome_message()
    menu()
    option = int(input("Enter your option here: "))


main_functions()