# rock-paper-scissors-exercise-2

Gain familiarity with the Python programming language, focusing on variables and conditional logic.
Learn how to process and validate user inputs in Python.
Learn how to import and access functionality provided by built-in Python modules and third-party Python packages.
Practice editing, saving, and executing local Python programs.
Practice incorporating version control into your local development process.

## Prerequisites

  + "Run the App" Excercise
  + Python Language Overview (focusing on Variables and Conditions)

## Instruction

Interactively develop a command-line Python application which will allow a human user to play a game of Rock-Paper-Scissors against a computer (NPC) opponent. The game's functionality should adhere to the "Requirements" below.

Before attempting to implement the basic requirements, take some time to configure your project repository according to the "Setup" instructions below. After doing so, you'll have a remote repo on GitHub and a local copy on your computer within which to develop.

When developing, as you reach key milestones, use the command-line or GitHub Desktop software to intermittently "commit", or save new versions of, your code. And remember to push / sync / upload your work back up to your remote project repository on GitHub at least once before you're done.

## Setup
Repo Setup
Use the GitHub online interface to create a new remote project repository called something like "rock-paper-scissors-exercise". When prompted by the GitHub online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub at an address like https://github.com/YOUR_USERNAME/rock-paper-scissors-exercise.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```
cd ~/Desktop/rock-paper-scissors-exercise1
```
Use your text editor or the command-line to create a file in that repo called "game.py", and then place the following contents inside:

```
# game.py

print("Rock, Paper, Scissors, Shoot!")
```
Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.


## Environment Setup
FYI: Only because we're going to be working with environment variables and requiring a third-party package called "python-dotenv" to read them from the ".env" file (see details below), we'll want to use a new project-specific Python environment within which to install any required packages. Otherwise we could do this exercise in the "base" environment.

Create and activate a new project-specific Anaconda virtual environment:

```
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```
From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

```
python game.py
```

If you see the "Rock, Paper, Scissors, Shoot!" message, you're ready to move on to project development. This would be a great time to make any desired modifications to your project's "README.md" file (like adding instructions for how to setup and run the app like you've just done), and then make your first commit, with a message like "Setup the repo".

## Requirements
Once you have completed the setup section above, you are ready to tackle the implementation of this exercise, as described by the sections below. To develop good version control habits, aim to make a separate commit after completing each section.

## Processing User Inputs
The application should prompt the user to input, or otherwise select, an option (i.e. "rock", "paper", or "scissors") via command-line interface (CLI). It should store the user's selection in a variable for later reference.

HINT: use the input() function to capture user inputs.

## Validating User Inputs
The application should compare the user's selection against the list of valid options (i.e. "rock", "paper", "scissors") to determine whether the user has selected a valid option.

If the selection is invalid, the program should fail gracefully by displaying a friendly message to the user, and preventing further program execution. The program should not try to further process an invalid input, as it may lead to runtime errors.

HINT: use the exit() or quit() keywords to stop the program.

## Simulating Computer Selection
The application should select one of the options (i.e. "rock", "paper", or "scissors") at random, and assign that as the computer player's choice.

HINT: use the choice() function provided by the random module.

HINT: ensure the valid choices are stored in a "list" datatype, and then pass that list to the random choice function.

## Determining the Winner
The application should compare the user's selection to the computer player's selection, and determine which is the winner. The following logic should govern that determination:

+ Rock beats Scissors
+ Paper beats Rock
+ Scissors beats Paper
+ Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"
    HINT: use one or more if statements (recommended approach for beginners), or it may also be possible to use a pre-configured "dictionary" datatype containing all possible outcomes.

## Displaying Results
After determining the winner, the application should display the results to the user. Desired information outputs (from start to finish) should include at least the following:

+ A friendly welcome message, including the player's name (by default, use "Player One").
+ The user's selected option
+ The computer's selected option
+ Whether the user or the computer was the winner
+ A friendly farewell message

Example desired output after one round of game-play:
```
-------------------
Welcome 'Player One' to my Rock-Paper-Scissors game...
-------------------
Please choose either 'rock', 'paper', or 'scissors': rock
You chose: 'rock'
The computer chose: 'paper'
-------------------
Oh, the computer won. It's ok.
-------------------
Thanks for playing. Please play again!
```

## Customizing the Player Name
Finally, update your program to allow the user to configure their own player name by passing an environment variable called "PLAYER_NAME" stored in a local ".env" file.

To do this, first create a .gitignore file in the repository if you haven't already. Make sure the repository's ".gitignore" file includes an entry about the ".env" file, and ensure the ".gigitnore" file is saved and committed before adding a ".env" file. This should already be the case if you added a Python-flavored ".gitignore" file during the repo creation step.

Then create a new file called "requirements.txt" 

The file's contents should include: 

python-dotenv # see: https://github.com/theskumar/python-dotenv

Next, in the command-line enter

```
pip install -r requirements.txt
```
This will install the dotenv environment to your python project.

Lastly, create a new file called ".env". Within the file add USER_NAME="PLAYER_NAME"

