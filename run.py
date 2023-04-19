import time
import os
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
    print(input("Press Enter to continue..."))
    clear_board()


welcome_message()


# Code from: https://www.youtube.com/watch?v=yriw5Zh406s&t=3s


def new_game():
    '''
    Starts a new game, displays each question in the game and the answers,
    cleans the terminal after each question is asked and answered,
    promps the user for the correct answer and stores the guesses of the users
    '''

    your_guesses = []
    correct_guesses = 0
    num_question = 1

    for key, value in questions.items():
        print()
        print(key)
        for i in choices[num_question-1]:
            print(i)
        guess = input("Enter here: ")
        guess = guess.upper()
        your_guesses.append(guess)

        clear_board()
        print()
        print(key)
        for i in choices[num_question-1]:
            print(i)
        time.sleep(3)
        print(f"The correct answer is: {value}")
        time.sleep(3)
        print()

        correct_guesses += check_answer(value, guess)
        num_question += 1

    show_score(correct_guesses, your_guesses)


def check_answer(your_answer, guess):
    '''
    Checks if the selected answers are correct,
    compares it to the right answers,
    if the answer is correct the user gets 1 point, if not then its 0
    '''

    if your_answer == guess:
        time.sleep(2)
        print(Fore.GREEN + "Well Done! Correct!")
        return 1
    else:
        print(Fore.RED + "Wrong!")
        return 0


# Code from: https://www.youtube.com/watch?v=yriw5Zh406s&t=3s


def show_score(correct_guesses, your_guesses):
    '''
    It shows the final results as the correct
    answers and the choices of the user
    '''
    print()
    print("FINAL RESULTS: ")
    time.sleep(2)
    print()

    print(Fore.GREEN + ("CORRECT ANSWERS: "), end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("YOUR GUESSES: ", end="")
    for guess in your_guesses:
        print(guess, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your final score is: "+str(score)+"%")

    if score == 100:
        print(Fore.CYAN + (
            "WOW! You are a genius. Excellent") + Style.RESET_ALL)
    elif score >= 70:
        print(Fore.YELLOW + (
            "Nice job! You have a good knowledge about swimming.") +
            Style.RESET_ALL)
    elif score >= 40:
        print(Fore.BLUE + (
            "Good effort! Try harder next time.") + Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + (
            "Unfortunately, you didn't do so well this time. "
            "Don't worry, keep practicing and "
            "I'm sure you'll do better next time") + Style.RESET_ALL)

    if play_another_game():
        clear_board()
        new_game()
    else:
        clear_board()


def play_another_game():
    '''
    Asks the user if they want to play again after getting their results
    and feedback on their performance in the game
    '''

    while True:
        response = input("Do you want to play again? (Y/N): ")
        if response.upper() == "Y":
            return True
        elif response.upper() == "N":
            return False
        else:
            print("Invalid input. Please enter Y or N.")

# Questions for the quiz


questions = {
    "Which of the following words refers to a swimming style?: ": "C",
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


# Code from: https://www.youtube.com/watch?v=63nw00JqHo0
def menu():
    '''
    A menu with three options for the player to choose from
    '''
    print("+-------------------------------------------+")
    print("+------------------MENU---------------------+")
    print("+-------------------------------------------+")
    print(" | Select one of the options from the menu: |")
    print("+-------------------------------------------+")
    print()
    print(" |                [1] Rules                 |")
    print(" |                [2] Play                  |")
    print(" |                [0] Quit                  |")
    print()


menu()
option = int(input("Enter your option here: "))

while option != 0:
    if option == 1:
        print("Displaying rules.....\n")
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
        print("Loading your quiz..... \n")
        time.sleep(5)
        print("Please wait...")
        time.sleep(3)
        new_game()
    else:
        print("Invalid option! Try again: ")
        time.sleep(1)

    print()
    menu()
    option = int(input("Enter your option here: "))

print("Thank you for playing! See you soon.")

while play_another_game():
    play_another_game()

print("Goodbye, see you soon!")


def main():
    '''
    Calls all functions
    '''
    welcome_message()
    new_game()
