# Swimming Quiz

pic..

Swimming is a popular recreational activity, sport, and form of exercise that involves propelling oneself through water using the arms and legs. It is a low-impact workout that offers numerous health benefits, such as improved cardiovascular health, increased muscular strength and endurance, and enhanced flexibility and range of motion. Swimming is also a lifesaving skill that can prevent drowning and other water-related accidents.
The swimming quiz is a test of knowledge and proficiency in various aspects of swimming, such as swimming strokes, techniques, rules, and safety measures. It includes multiple-choice questions. The quiz may be taken by beginners or experienced swimmers and covers topics such as freestyle, backstroke, breaststroke, butterfly, and flip turns. The purpose of the quiz is to assess one's knowledge and understanding of swimming and to promote safe and effective swimming practices.

<br>
<br>

## Table of Contents
1. [User Experience (UX)](#user-experience-UX)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Color Scheme](#color-scheme)
    4. [Flowchart](#flowchart)
2. [Features](#features)

<br>
<br>

## User Experience (UX)

<br>

### Project Goals

<br>

* Display clear information about the swimming quiz in order to make it easy to understand even for first time users.
* Each step provides the necessary information to make the program clear and intuitive.
* Provide input validation to help the user to input the correct data throughout the quiz.
* The program should keep running until the user decides otherwise.
* Provide the user with a fun, engaging and easy to play multiple choice quiz.
* Provide some visuals with the use of ascrii art and colour to contribute to a positive user experience.
* Accurately keep track of and display the user’s score clearly at the end of the quiz. 

<br>
<br>

### User Stories

<br>

* As a user, I want to receive information about the main objective of the program.
* As a user, I want to easily understand what input is needed on each step.
* As a user, I want to receive clear feedback in case I provide the wrong input.
* As a user, I want the results to be displayed in a clear way and to be easy to understand.
* As a user, I want to be able to easily repeat the quiz if I want to try again.

<br>
<br>

### Color Scheme

<br>

[Colorama](https://pypi.org/project/colorama/) has been used to apply color to the terminal text and the logo,
in order to make it more intuitive and easier to read.

* Wrong answers are in red colour.
* Correct answers are in green colour.
* The logo of the game is in blue with white background colour.
* Messages are displayed in the default terminal color.
* The feedback at the end of the game is displayed with a different colours depending on the % the user gets at the end. 
    The colours used for the different messages are: Cyan, Green, Yellow, Blue and Magenta.

<br>
<br>

### Flowchart

<br>

[Lucid](https://www.lucid.app/) has been used to create a simple flowchart of the expected flow of logic through the programme from start to finish. This helped me to visualise the structure of the code and what functions may be needed. 

![Swimming Quiz Flowchart] (https://res.cloudinary.com/doyc0uqcs/image/upload/v1682527380/Project%203%20Swimming%20Quiz/lucid_chart_ytjq15.png)

As shown in the flowchart, the original order of some functions has been changed during the development process in order to follow a more intuitive logic and sequence of events but the main idea behind the process is still the same.

<br>
<br>

## Existing Features

<br>
<br>

### Welcome Logo

<br>

- The welcome logo when you start the game.

![logo](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682529373/Project%203%20Swimming%20Quiz/swimming_Logo_bzk6yu.png) 

<br>
<br>

### Welcome Message and User Input

<br>

- Welcome message and user input for their name to continue to the main.

![message](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682529613/Project%203%20Swimming%20Quiz/welcome_message_and_name_glrqzg.png)

<br>
<br>

### Menu

<br>

- Main Menu after the user inputs their name.
- The user has 4 options to choose from.
- If they select option 1, the rules pop up.
- If they select option 2, the game starts.
- If they select option 3, the leaderboard shows up.
- Only 3 people have played the game so far.
- The leaderboard shows top 5 scores only.
- if they select option 0, the game quits.

<br>
<br>

- Menu:

<br>

![menu](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530127/Project%203%20Swimming%20Quiz/Main_Menu_wixifz.png)

<br>
<br>

- Option 1:

<br>

![option1](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530200/Project%203%20Swimming%20Quiz/rules_of_the_game_n9urzr.png)

<br>
<br>

- Option 2:

<br>

![option2](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530356/Project%203%20Swimming%20Quiz/the_quiz_lysudn.png)

<br>
<br>

- Option 3:

<br>

![option3](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530628/Project%203%20Swimming%20Quiz/leaderboard_thobcg.png)

<br>
<br>

- Option 0:

<br>

![option0](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530755/Project%203%20Swimming%20Quiz/press_0_rjxllm.png)

<br>
<br>

### Results

<br>

- When the user finishes the last question,
    the results show up.
- The user guesses and their score is calculated.
- The correct answers of the game are shown.
- The user gets a feedback message at the end as well.
- Depending on the % that the user got, the colour of the feedback message changes.
- After the results, the score and the name of the user is exported to Google worksheet and a message to acknowledge this is displayed.
- Lastly, there is a question that asks the user if they would like to play another game. If they say "Y", it brings them back to the menu and they can select whatever option they like. If they say "N", a goodbye message is displayed.

<br>
<br>

- Results:

<br>

![results](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682531050/Project%203%20Swimming%20Quiz/results_kak0s7.png)

<br>
<br>

- Score Worksheet:

<br>

![exporting](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682531189/Project%203%20Swimming%20Quiz/exporting_to_google_sheets_pn7zne.png)

<br>
<br>

- Question:

<br>

![question](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682531313/Project%203%20Swimming%20Quiz/another_game_fnflzl.png)
