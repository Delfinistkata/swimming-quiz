# Swimming Quiz

pic..

Swimming is a popular recreational activity, sport, and form of exercise that involves propelling oneself through water using the arms and legs. It is a low-impact workout that offers numerous health benefits, such as improved cardiovascular health, increased muscular strength and endurance, and enhanced flexibility and range of motion. Swimming is also a lifesaving skill that can prevent drowning and other water-related accidents.
The swimming quiz is a test of knowledge and proficiency in various aspects of swimming, such as swimming strokes, techniques, rules, and safety measures. It includes multiple-choice questions. The quiz may be taken by beginners or experienced swimmers and covers topics such as freestyle, backstroke, breaststroke, butterfly, and flip turns. The purpose of the quiz is to assess one's knowledge and understanding of swimming and to promote safe and effective swimming practices.

<br>
<br>

# Table of Contents
1. [User Experience (UX)](#user-experience-UX)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Color Scheme](#color-scheme)
    4. [Flowchart](#flowchart)
2. [Features](#features)
    1. [Welcome Message and User Input](#welcome-message-and-user-input)
    2. [Menu](#menu)
    3. [Results](#results)
3. [Technologies Used](#technologies-used)
    1. [Language Used](#language-used)
    2. [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
4. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Code Validation](#code-validation)
    3. [Manual Testing](#manual-testing)
5. [Deployment](#deployment)



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
- After the results, the score and the name of the user is exported to Google worksheet 
    and a message to acknowledge this is displayed.
- Lastly, there is a question that asks the user if they would like to play another game. 
    If they say "Y", it brings them back to the menu and they can select whatever option they like. 
    If they say "N", a goodbye message is displayed.

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

## Technologies Used

<br>
<br>

### Language Used

<br>

* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

<br>

### Frameworks, Libraries and Programs Used

<br>

* [GitPod](https://gitpod.io/) was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/) was used to store the project after pushing.

* [Heroku](https://id.heroku.com/) was used to deploy the application.

* [PEP8 online check](https://pep8ci.herokuapp.com/) was used to validate the Python code.

* [Colorama](https://pypi.org/project/colorama/) library was used to apply color to the terminal text.

* [Ascrii Art](https://www.asciiart.eu/) was used for the welcome logo

<br>
<br>

## Testing

<br>

### Testing User Stories

<br>

* As a user, I want to receive information about the main objective of the program.

    - Information about the program is presented in the welcome message.
    - Further information about the quiz can be found under option 1 (rules).

<br>

* As a user, I want to easily understand what input is needed on each step.

    - Input messages are being provided with detailed information on what the input needs to be.

<br>

* As a user, I want to receive clear feedback in case I provide the wrong input.

    - Error messages are provided explaining what is wrong with the input provided in case the wrong input is entered.

<br>

* As a user, I want the results to be displayed in a clear way and to be easy to understand.

    - Option 3 (Leaderboard) provides the name and the results from the quiz for the top 5 people only.

<br>

* As a user, I want to be able to easily repeat the quiz if I want to try again.

    - At the end of the quiz, the user has the option to say yes if they would like to play again. Once they reply with Yes, it will bring them back to the menu and they can select from the 4 options available.

<br>
<br>

### Code Validation

<br>

The [PEP8 online check](https://pep8ci.herokuapp.com/) was used throughout the development process to validate the Python code for PEP8 requirements. No errors were found after the last test.

<br>

![PEP8 Code Validation](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682598758/Python_Linter_results_o0rlya.png)

<br>
<br>

### Manual Testing

<br>

<table>
    <tr>
        <th>Feature</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Name Input</td>
        <td>Validate if value is empty</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Enter Input</td>
        <td>Validate if value is a empty</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Question Input</td>
        <td>Validate if invalid value</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Restart the game</td>
        <td>Keep running or exit the program</td>
        <td>Pass</td>
    </tr>
</table>

<br>
<br>

[Back to top ⇧](#swimming-quiz)

<br>

## Deployment

<br>

- Deployment was done at the start of the project to allow device testing throughout the development process.
- The application has been deployed using [Heroku](https://id.heroku.com/) by the following steps:

<br>
<br>

1. Remove un-used imports from run.py file.
2. In order for input methods to work properly in the deployed mock terminal, add a new line character at the end of the text, inside the input method. 
3. Create the requirements.txt file and run: `pip3 freeze > requirements.txt` in the console.
4. Commit changes and push them to GitHub.
5. Go to the Heroku's website.
6. From the Heroku dashboard, click on "Create new app".
7. Enter the "App name" and "Choose a region" before clicking on "Create app".
8. Go to "Config Vars" under the "Settings" tab.
9. Click on "Reveal Config Vars" and add the KEY: CREDS and the VALUE stored in creds.json file if needed.
10. Add the Config Var, KEY: PORT and VALUE: 8000.
11. Go to "Buildpacks" section and click "Add buildpack".
12. Select "python" and click "Save changes".
13. Add "nodejs" buildpack as well using the same process.
14. Go to "Deployment method", under the "Deploy" tab select "GitHub" and click on "Connect to GitHub".
15. Go to "Connect to GitHub" section and "Search" the repository to be deployed.
16. Click "Connect" next the repository name.
17. Choose "Automatic deploys" or "Manual deploys" to deploy your application.

<br>

[Back to top ⇧](#swimming-quiz)

<br>