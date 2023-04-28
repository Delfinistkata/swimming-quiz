<br>

# **Swimming Quiz**

<br>
<br>

![responsive-pic](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682690487/Project%203%20Swimming%20Quiz/responsivepic_yz5h65.png)

<br>
<br>

The swimming quiz is a test of knowledge and proficiency in various aspects of swimming, such as swimming strokes, techniques, rules, and safety measures. It includes multiple-choice questions. The quiz can be taken by anyone and covers topics such as freestyle, backstroke, breaststroke, butterfly, and flip turns. The purpose of the quiz is to assess one's knowledge and understanding of swimming and to promote safe and effective swimming practices.

<br>
<br>

The live link can be found [here]()

<br>
<br>

# Table of Contents

## [User Experience UX](<#user-experience-ux-1>)
1. ### [Project Goals](<#project-goals-1>)
2. ### [User Stories](<#user-stories-1>)
3. ### [Colour Scheme](#colour-scheme-1)
4. ### [Data Model](#data-model-1)
5. ### [Flowchart](#flowchart-1)

## [Existing Features](<#existing-features-1>)
1. ### [Welcome Message and User Input](#welcome-message-and-user-input-1)
2. ### [Menu](#menu-1)
3. ### [Results](#results-1)

## [Technologies Used](#technologies-used-1)
1. ### [Language Used](#language-used-1)
2. ### [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used-1)

## [Testing](#testing-1)
1. ### [Testing User Stories](#testing-user-stories-1)
2. ### [Code Validation](#code-validation-1)
3. ### [Manual Testing](#manual-testing-1)

## [Deployment](#deployment-1)

## [Credits](#credits-1)
1. ### [Content](<#content-1>)
2. ### [Media](<#media-1>)

## [Acknowledgements](#acknowledgements)

<br>
<br>

# User Experience UX

<br>

## Project Goals

<br>

* Display clear information about the swimming quiz in order to make it easy to understand even for first time users.
* Each step provides the necessary information to make the program clear and intuitive.
* Provide input validation to help the user to input the correct data throughout the quiz.
* The program should keep running until the user decides otherwise.
* Provide the user with a fun, engaging and easy to play multiple choice quiz.
* Provide some visuals with the use of ASCII art and colour to contribute to a positive user experience.
* Accurately keep track of and display the user’s score clearly at the end of the quiz. 

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

## User Stories

<br>

* As a user, I want to receive information about the main objective of the program.
* As a user, I want to easily understand what input is needed on each step.
* As a user, I want to receive clear feedback in case I provide the wrong input.
* As a user, I want the results to be displayed in a clear way and to be easy to understand.
* As a user, I want to be able to easily repeat the quiz if I want to try again.

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

## Colour Scheme

<br>

[Colorama](https://pypi.org/project/colorama/) has been used to apply colour to the terminal text and the logo,
in order to make it more intuitive and easier to read.

* Wrong answers are in red colour.
* Correct answers are in green colour.
* Invalid inputs/options are in red colour.
* The logo of the game is in blue with white background colour.
* Messages are displayed in the default terminal colour.
* Updating the Google sheet message at the end of the game is in green colour.
* The feedback at the end of the game is displayed with different colours depending on the % the user gets at the end. 
    The colours used for the different messages are: Cyan, Green, Yellow, Blue and Magenta.

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

## Data Model

<br>

- The check_answer() function checks if the selected answer is correct, compares it to the correct answer, and returns either 1 or 0.

- The new_game() function starts a new game, displays each question in the game and the possible answers, prompts the user for the correct answer, and stores the user's guesses.

- The your_guesses variable is a list that will store the user's guesses for each question.

- The correct_guesses variable keeps track of how many questions the user answered correctly.

- The num_question variable is an integer that keeps track of the current question number.

- The questions are stored in a dictionary and the optional answers are stored in a list, which means that more questions can be added to this quiz in the future along with the optional answers

- The show_score() function displays the user's score and their guesses for each question.

- The import_results_worksheet() function imports the data from the "total_score" sheet using the get_all_values() method of the worksheet object of the SHEET object.

- The export_results_worksheet() function exports the user's name and score to a Google Sheets document after each game.

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>


## Flowchart

<br>

[Lucid](https://www.lucid.app/) has been used to create a simple flowchart of the expected flow of logic through the programme from start to finish. This helped me to visualise the structure of the code and what functions may be needed. 

<br>

![Flowchart](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682527380/Project%203%20Swimming%20Quiz/lucid_chart_ytjq15.png)

<br>

As shown in the flowchart, the original order of some functions has been changed during the development process in order to follow a more intuitive logic and sequence of events but the main idea behind the process is still the same.

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

# Existing Features

<br>
<br>

## Welcome Logo

<br>

- The welcome logo when you start the game.

![logo](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682687073/Project%203%20Swimming%20Quiz/welcome_logo_1_ksuq84.png) 

<br>
<br>

## Welcome Message and User Input

<br>

- Welcome message and user input for their name to continue to the main.

![message](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682529613/Project%203%20Swimming%20Quiz/welcome_message_and_name_glrqzg.png)

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

## Menu

<br>

- Main Menu after the user inputs their name.
- The user has 4 options to choose from.
- If they select option 1, the rules pop up.
- If they select option 2, the game starts.
- If they select option 3, the leaderboard shows up.
- The leaderboard shows top 5 scores only.
- If they select option 0, the game quits.

<br>
<br>

- Menu:

    * As a user I want to clearly see and use the options from the menu.

<br>

![menu](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530127/Project%203%20Swimming%20Quiz/Main_Menu_wixifz.png)

<br>
<br>

- Option 1:

    * As a user I want clear instructions on how to use the quiz.

<br>

![option1](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530200/Project%203%20Swimming%20Quiz/rules_of_the_game_n9urzr.png)

<br>
<br>

- Option 2:

    * As a user I want to test my knowledge of swimming.
    * As a user I want to be able to read the application output clearly.

<br>

![option2](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530356/Project%203%20Swimming%20Quiz/the_quiz_lysudn.png)

<br>
<br>

- Option 3:

    * As a user I want to clearly see the leaderboard.

<br>

![option3](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682611164/Project%203%20Swimming%20Quiz/leaderboard11_gxsmjr.png)

<br>
<br>

- Option 0:

    * As a user I want to quit the game.

<br>

![option0](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530755/Project%203%20Swimming%20Quiz/press_0_rjxllm.png)

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

## Results

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

    * As a user I want to clearly see my score at the end of the quiz.

<br>

![results](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682531050/Project%203%20Swimming%20Quiz/results_kak0s7.png)

<br>
<br>

- Score Worksheet:

    * As a user I want to know if my name and score has been recorded.

<br>

![exporting](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682531189/Project%203%20Swimming%20Quiz/exporting_to_google_sheets_pn7zne.png)

<br>
<br>

- Question:

    * As a user I want to be able to easily repeat the quiz if I want to try again.

<br>

![question](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682531313/Project%203%20Swimming%20Quiz/another_game_fnflzl.png)

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

# Technologies Used

<br>
<br>

## Language Used

<br>

* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

<br>

## Frameworks, Libraries and Programs Used

<br>

* [GitPod](https://gitpod.io/) was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/) was used to store the project after pushing.

* [Heroku](https://id.heroku.com/) was used to deploy the application.

* [PEP8 online check](https://pep8ci.herokuapp.com/) was used to validate the Python code.

* [Colorama](https://pypi.org/project/colorama/) library was used to apply colour to the terminal text.

* [Gspread](https://docs.gspread.org/en/v5.7.1/) module was used for Google sheets.

* [Time](https://www.programiz.com/python-programming/time) module was used for delaying the output.

* [Ascrii Art](https://www.asciiart.eu/) was used for the welcome logo.

* [Responsive Design Checker](https://www.responsivedesignchecker.com/) was used to generate mock-up imagery.

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

# Testing

<br>

## Testing User Stories

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

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

## Code Validation

<br>

The [PEP8 online check](https://pep8ci.herokuapp.com/) was used throughout the development process to validate the Python code for PEP8 requirements. No errors were found after the last test.

<br>

![PEP8 Code Validation](https://res.cloudinary.com/doyc0uqcs/image/upload/v1682689027/Project%203%20Swimming%20Quiz/validation_CI_ko06qk.png)

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

## Manual Testing

<br>

<table>
    <tr>
        <th>Feature</th>
        <th>Outcome</th>
        <th>Example</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td>Name Input</td>
        <td>Validate if value is empty</td>
        <td><a href="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682690875/Project%203%20Swimming%20Quiz/nameinput_jdsjtg.png"><img src="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682690875/Project%203%20Swimming%20Quiz/nameinput_jdsjtg.png" alt="name"></a></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Enter Input</td>
        <td>Validate if invalid value</td>
        <td><a href="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682692271/Project%203%20Swimming%20Quizenterpress_smq4ed.png"><img src="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682692271/Project%203%20Swimming%20Quiz/enterpress_smq4ed.png" alt="enter"></a></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Question Input</td>
        <td>Validate if invalid value</td>
        <td><a href="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682693152/Project%203%20Swimming%20Quiz/questionsinput_jzm9ml.png"><img src="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682693152/Project%203%20Swimming%20Quiz/questionsinput_jzm9ml.png" alt="question"></a></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td>Try again Input</td>
        <td>Validate if invalid value</td>
        <td><a href="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682697144/Project%203%20Swimming%20Quiz/yesnoinput_ijnqlu.png"><img src="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682697144/Project%203%20Swimming%20Quiz/yesnoinput_ijnqlu.png" alt="try-again"></a></td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=4>Restart the game</td>
        <td rowspan=4>Keep running or exit the program</td>
        <td><a href="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682694285/Project%203%20Swimming%20Quiz/yn_whyxxx.png"><img src="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682694285/Project%203%20Swimming%20Quiz/yn_whyxxx.png" alt="yes/y"></a></td>
        <td rowspan=4>Pass</td>
    </tr>
    <tr>
        <td><a href="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530127/Project%203%20Swimming%20Quiz/Main_Menu_wixifz.png"><img src="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530127/Project%203%20Swimming%20Quiz/Main_Menu_wixifz.png" alt="menu"></a></td>
    </tr>
    <tr>
        <td><a href="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682695110/Project%203%20Swimming%20Quiz/noyes_riar2k.png"><img src="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682695110/Project%203%20Swimming%20Quiz/noyes_riar2k.png" alt="no/n"></a></td>
    </tr>
    <tr>
        <td><a href="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530755/Project%203%20Swimming%20Quiz/press_0_rjxllm.png"><img src="https://res.cloudinary.com/doyc0uqcs/image/upload/v1682530755/Project%203%20Swimming%20Quiz/press_0_rjxllm.png" alt="quit"></a></td>
    </tr>
</table>

<br>

[Back to top ⇧](#swimming-quiz)

<br>
<br>

# Deployment

<br>

- Deployment was done at the start of the project to allow device testing throughout the development process.
- The application has been deployed using [Heroku](https://id.heroku.com/) by the following steps:

<br>
<br>

1. Remove unused imports from run.py file.
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
16. Click "Connect" next to the repository name.
17. Choose "Automatic deploys" or "Manual deploys" to deploy your application.

<br>

The live link can be found [here]()

<br>

[Back to top ⇧](#swimming-quiz)

<br>

# Credits

<br>

## Content

<br>

[Stackoverflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python) was used for clearing the terminal.

[Programiz](https://www.programiz.com/python-programming/time/sleep) was used for the pause between the questions and loading of the results and the leaderboard.

[Youtube](https://www.youtube.com/watch?v=wVXYqHuWC_s&t=409s) was used for the importing of the data from Google sheets.

[Youtube](https://www.youtube.com/watch?v=9xmfi4kKMPM) was used for exporting of the data to Google sheets.

[Youtube](https://www.youtube.com/watch?v=63nw00JqHo0) was used for creating the layout of the menu.

[We Love Quizzes](https://www.welovequizzes.com/swimming-quiz-question-and-answers/) was used for the questions in the game.

[Readme.md](https://github.com/josswe26/macro-calculator/blob/main/README.md) was used for some ideas.

[Coudinary](https://cloudinary.com/) : was used to store the screenshots in the Readme file.

[Colorama](https://pypi.org/project/colorama/) was used for the colour of the text in the game.

[Responsive Design Checker](https://www.responsivedesignchecker.com/) was used to generate mock-up imagery.

[Lucid](https://www.lucid.app) was used for the flowchart of the game.

<br>

## Media

<br>

[ASCII-Generator](https://ascii-generator.site/) was used for the welcome logo.

<br>

**[Back to top ⇧](#swimming-quiz)**

<br>
<br>

## Acknowledgements

<hr>
<br>

This project was developed and designed as a Portfolio 3 Project for Full Stack Software Developer Diploma course at the [Code Institute](https://codeinstitute.net/). I would like to thank my mentor Marcel Mulders for his invaluable feedback and guidance, our facilitator Chris Quinn, the Slack community, and all at the Code Institute for their help and support. I really enjoyed working on this project.

<br>
<br>

**[Back to top ⇧](#swimming-quiz)**