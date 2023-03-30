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


# Code from: https://www.youtube.com/watch?v=63nw00JqHo0
def menu():
    '''
    A menu with three options for the player to choose from
    '''
    print("Select one of the options from the menu: ")
    print("[1] Rules")
    print("[2] Play")
    print("[0] Quit")


menu()
option = int(input("Enter your option here: "))

while option != 0:
    if option == 1:
        print("Displaying rules..... \n")
        time.sleep(4)
        print("Please wait...")
        time.sleep(2)
        print()
        rules = [
            "The player is presented with a question and 4 answers.\n",
            "The player will have a hint before answering.\n",
            "The player answers by entering the correct letter.\n",
            "If you select the correct answer, you earn a point.\n",
            "If the answer is incorrect, no points are earned.\n",
            "This continues until all questions are answered.\n",
            "At the end of the game, the player's score is displayed.\n"
        ]
        for rule in rules:
            print(rule)
            time.sleep(3)
    elif option == 2:
        print("play now")
        time.sleep(2)
    else:
        print("Invalid option! Try again: ")
        time.sleep(1)

    print()
    menu()
    option = int(input("Enter your option here: "))

print("Thank you for playing! See you soon.")


# Questions for the quiz

questions = {
    "Which of the following wrods refers to a swimming style?: ": "C",
    "How many strokes are performed during competitions?: ": "B",
    "In a relay, how many swimmers are there in each team?: ": "A",
    "At which age did Ian Thrope become the youngest world champion?: ": "A",
    "Which stroke is considered to be the most difficult?: ": "C",
    "Where is the headquarters of FINA located?: ": "B",
    "What is the benefit of wearing a swim cap?: ": "B",
    "What does IM stands for?: ": "B",
    "Which is the slowest stroke?: ": "A",
    "Who won titles in American, British, European and Olympic races?: ": "A",
    "When did swimming first become part of the Olympic Summer Games?: ": "A",
    "The freestyle was developed based on a swimming style in?: ": "B",
    "How long is a lap in an Olympic-sized swimming pool?: ": "A",
    "What is the only open water event in the Olympics?: ": "B",
    "In swimming competitions, what's the limit for swimsuits on legs?: ": "B",
}

# Optional answers for the quiz

choices = [
    ["A. A pull", "B. A kick", "C. A stroke"],
    ["A. 3", "B. 4", "C. 5"],
    ["A. 4", "B. 3", "C. 5"],
    ["A. 15", "B. 17", "C. 19"],
    ["A. Breaststroke", "B. Backstroke", "C. Butterfly"],
    ["A. Nice, France", "B. Lausanne, Switzerland", "C. Hamburg, Germany"],
    ["A. To improve look", "B. To reduce drag", "C. To protect hair"],
    ["A. International Master", "B. Individual Medley", "C. Internal Meeting"],
    ["A. Breaststroke", "B. Backstroke", "C. Butterfly"],
    ["A. David Wilkie", "B. John Hencken", "C. Gunnar Larsson"],
    ["A. 1896", "B. 1926", "C. 1934"],
    ["A. Fiji", "B. Solomon Islands", "C. Marshall Islands"],
    ["A. 50m", "B. 75m", "C. 100m"],
    ["A. 5km", "B. 10km", "C. 25km"],
    ["A. Thighs", "B. Knees", "C. Ankles"],
]