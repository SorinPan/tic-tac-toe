# Tic Tac Toe

![Responsive view of the game](docs/am-i-responsive.png)

Tic Tac Toe is a simple terminal game that can be played against another player or against the computer. The gameboard is grid of 3 squares by 3 squares. The players choose their marks between X and O and then take turns placing their marks on the empty squares. The goal of the game is to place 3 marks in a row (up, down, across or diagonally).

[View Live Site](https://tic-tac-toe-g-e198203b2fcd.herokuapp.com)

---

## Contents

---

## User Experience (UX)

### User Stories

#### Target Audience

Tic Tac Toe is a classic game and it's fun for all ages.

#### First Time Users

- As a first time user, I want to easily understands the purpose of the game.
- As a first time user, I want to be able to see clear instructions on how to play.
- As a first time user, I want to be able to play against another player or computer.
- As a first time user, I want to choose my mark (X - O).
- As a first time user, I want to be notified when making an invalid move.
- As a first time user, I want to be able to play again and quit the game.
- As a first time user, I want to se my score after the game ends.

#### Returning Users

- As a returning user, I want to easily start a new game.
- As a returning user, I want to see the last top scores.

### Goals

- Easy and intuitive gameplay. Providing enough instructions so the users can play the game without confusion.
- Giving clear and informative feedback to the user after each move.
- Easy menu navigation.
- Input validation. Prompt the users when invalid moves or inputs are made.
- Top scores. The users should be able to see the last top scores.


## Design


### Flowchart

![Logic Flowchart](docs/flowchart.png)

## Features

### Existing Features

#### Main Menu

When the user starts the aplication they first see the Logo and Main Menu. Here the user can choose to start the game or see the instructions.

![Main Menu feature](docs/features/main-menu-feat.png)

#### Instructions

The user can choose to see the instructions of the game from the main menu.

![Instructions feature](docs/features/instructions-feat.png)

#### Multiplayer option

When the game starts, the user can input their name and then choose to play against computer or another player.

![Multiplayer option feature](docs/features/options-feat.png)

#### Game Over

After the five rounds are played, the game is over. The top scores are then updated with the winner's name, score and date.

![Game Over feat](docs/features/game-over-feat.png)

#### Top Scores

After the top scores are updated. A list of the highest 10 top scores will be displayed.

![Top Scores feature](docs/features/top-scores-feat.png)

### Future Features

- Add some more colors to the text so it will be easier for the user to see the game context.
- Make the Computer smarter. Right now it chooses the moves only randomly.
- Add a quit option after each round.

## Testing

### Python Validation

Used Code Institute's own python validator [CI Python Linter](https://pep8ci.herokuapp.com/)
For some reason it doesn't like white spaces.

<details><summary>Python</summary>
<img src="docs/python-validation.png">
</details>

### Testing user stories

#### First time Users

Understanding the Purpose**
  * As a first time user, I want to understand the purpose of the game from the moment I launch it.
  * **Test**: Launch the game and check if the main menu displays clear instructions about the game's objective.
* **Clear Instructions**
  * As a first time user, I want to find clear instructions on how to play the game.
  * **Test**: Access the instructions from the main menu and verify that the rules and gameplay are explained concisely and comprehensively.
* **Choose Opponent and Mark**
  * As a first time user, I want to be able to choose between playing against another player or the computer.
  * **Test**: Start a new game and check if the game prompts to choose an opponent, and verify that selecting "Computer" or "Player 2" sets up the correct gameplay.
* **Selecting My Mark**
  * As a first time user, I want to choose my preferred mark (X or O) before starting the game.
  * **Test**: Begin a new game and ensure that the game asks for the player's preferred mark and uses it correctly throughout the game.
* **Invalid Move Notification**
  * As a first time user, I want to be notified when attempting to make an invalid move (e.g., selecting an already occupied position).
  * **Test**: During gameplay, intentionally make an invalid move and verify that the game displays an appropriate error message and prompts the user to make a valid move.
* **Play Again and Quit**
  * As a first time user, I want the option to play again or quit the game after a round ends.
  * **Test**: Finish a game round and check if the game prompts the user to play again or quit, and verify that selecting "play again" restarts the game.
* **Score Display**
  * As a first time user, I want to see my score after the game ends.
  * **Test**: Play multiple rounds, ensuring that the game displays the final score between the players at the end of each round.

#### Returning Users
* **Starting a New Game**
  * As a returning user, I want to easily start a new game without any hassle.
  * **Test**: After finishing a game, check if the game provides an option to start a new game from the main menu without any issues.
* **Top Scores**
  * As a returning user, I want to view the last top scores achieved by different players.
  * **Test**: After several rounds of gameplay, verify that the game shows the top scores on the leaderboard and updates it accordingly.

#### General Goals

* **Intuitive Gameplay**
  * As a user, I expect the gameplay to be easy and intuitive.
  * **Test**: Play multiple rounds and observe if the game mechanics are straightforward and require minimal effort to understand.
* **Clear Feedback**
  * As a user, I want the game to provide clear and informative feedback after each move.
  * **Test**: During gameplay, verify that the game displays appropriate messages after each move, indicating whether it was successful or not.
* **Menu Navigation**
  * As a user, I expect easy navigation through the game's menu.
  * **Test**: Test the menu options, making sure that users can easily navigate between starting a game, accessing instructions, and viewing top scores.
* **Input Validation**
  * As a user, I want the game to handle invalid inputs gracefully.
  * **Test**: Attempt to input invalid moves or characters during gameplay and check if the game responds with appropriate error messages.
* **Top Scores Visibility**
  * As a user, I want to easily access the last top scores achieved in the game.
  * **Test**: Verify that the game displays the last top scores prominently and provides a clear view of the players' names, scores, and dates.

## Bugs

- Clears the terminal screen too quickly and doesn't show when the computer makes a move.

## Technologies Used

### Languages

- [Python](https://www.python.org)

### Libraries

- [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random) - Used for the Computer moves.

### Tools

- [GitHub](https://github.com) - Used for storing the code.
- [Git](https://git-scm.com) - Used for version control.
- [VSCode](https://code.visualstudio.com) - Used to develop the game.
- [LucidChart](https://www.lucidchart.com/pages/) - Used for making flowcharts.
- [Pipenv](https://docs.python-guide.org/dev/virtualenvs/) - For creating virtual environment and installing packages.
- [CI Template](https://github.com/Code-Institute-Org/p3-template) - Used when creating the repository on GitHub.
- [Bear](https://bear.app) - For planning the development, keeping notes and ideas.

## Deployment

## Development

### How to Fork

To Fork this project:

1. Log in to GitHub.
2. Go to the project's repository [Tic-Tac-Toe](https://github.com/SorinPan/tic-tac-toe/tree/main).
3. Click on the Fork button at the top.

### How to Clone

To Clone this project:

1. Log in to GitHub.
2. Go to the project's repository [Tic-Tac-Toe](https://github.com/SorinPan/tic-tac-toe/tree/main)
3. Click on the <> Code button at the top of the file list.
4. Choose to clone using either HTTPS, SSH key or GitHub CLI, then copy the link provided.
5. Go to your code editor and open a Terminal.
6. Change the current working directory to the location where you want the cloned directory.
7. Type in git clone, then press "Spacebar" and paste the link you copied earlier.
8. Press "Enter" to create your clone repository.

## Credits

[How to clear the screen](https://www.geeksforgeeks.org/clear-screen-python/)
[Readme](https://github.com/kera-cudmore/readme-examples/tree/main)
[W3Schools](https://www.w3schools.com/python/)
https://www.w3schools.com/python/ref_func_enumerate.asp
[Python DateTime Format Using Strftime\(\)](https://pynative.com/python-datetime-format-strftime/)
[Tic-tac-toe using Python](https://www.askpython.com/python/examples/tic-tac-toe-using-python) - For inspiration.

## Comments
