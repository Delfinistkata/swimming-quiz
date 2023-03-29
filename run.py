import gspread
from google.oauth2.service_account import Credentials
import random
import os
import time
import textwrap
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

    print(reset_all + 'Welcome to the swimming quiz!\n')