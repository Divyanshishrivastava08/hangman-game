Hangman Game – Project Statement

1. Problem Statement

Hangman is a word-guessing game in which the player has to guess a hidden word by entering one letter at a time. The player has a limited number of wrong attempts. If the player guesses all the letters correctly before the maximum number of wrong guesses is reached, the player wins. Otherwise, the game ends with a "Game Over" message.

The purpose of this project is to develop a simple and interactive Hangman Game using Python. The project demonstrates basic programming concepts such as variables, lists, loops, conditional statements, functions of Python's built-in features, user input, string manipulation, and the "random" module.

The game randomly selects a word from a predefined list and allows the player to guess the word letter by letter. The program also displays a Hangman drawing that changes according to the number of incorrect guesses.

---

2. Scope of the Project

The scope of this project is to create a command-line based Hangman game that is simple, interactive, and easy to play.

The project includes:

- A large predefined list of words.
- Random selection of a word using Python's "random" module.
- Letter-by-letter word guessing.
- Display of correctly guessed letters.
- Display of hidden letters using underscores.
- A maximum of 6 wrong guesses.
- Progressive Hangman drawings based on wrong guesses.
- Input validation to ensure that the player enters only one alphabetic character.
- Detection of repeated guesses.
- Win and Game Over conditions.
- Display of the correct word when the game ends.

The current version is designed for a single player and runs in the Python terminal.

---

3. Target Users

The target users of this project are:

- Beginners who want to learn Python programming.
- Students learning basic programming concepts.
- Users who enjoy simple word-guessing games.
- Students who want to understand how interactive programs work.
- Beginners learning concepts such as loops, lists, strings, conditions, and random selection.

---

4. High-Level Features

4.1 Random Word Selection

The game uses Python's "random" module to select a word randomly from the predefined word list.

4.2 Hidden Word Display

The letters of the selected word are hidden from the player. Correctly guessed letters are displayed while unguessed letters are represented using underscores.

4.3 Letter Guessing

The player enters one letter at a time to try to reveal the hidden word.

4.4 Input Validation

The program checks whether the player has entered exactly one alphabetic character. Invalid inputs are rejected and the player is asked to enter a valid letter.

4.5 Repeated Guess Detection

If the player enters a letter that has already been guessed, the program displays a message and does not count it as a wrong attempt.

4.6 Hangman Drawing

The game contains different Hangman drawings for each stage of the game. The drawing becomes more complete as the number of wrong guesses increases.

4.7 Wrong Guess Tracking

The program keeps track of the number of incorrect guesses. The maximum number of wrong guesses allowed is 6.

4.8 Winning Condition

The player wins when all the letters of the selected word have been correctly guessed.

4.9 Game Over Condition

If the player reaches 6 wrong guesses before completing the word, the game ends and the correct word is displayed.

4.10 User-Friendly Terminal Output

The game provides clear messages such as:

- Correct guess
- Wrong guess
- Already guessed letter
- Invalid input
- Congratulations
- Game Over

This makes the game simple and easy to understand.

---

5. Technologies Used

- Programming Language: Python
- Module Used: "random"
- Interface: Command Line / Terminal
- Version Control: Git and GitHub

---

6. Project Objective

The main objective of this project is to create a simple interactive game while applying fundamental Python programming concepts.

Through this project, the developer can practice:

- Lists
- Strings
- Variables
- Loops
- Conditional statements
- User input
- Input validation
- Random selection
- Basic problem-solving
- GitHub project management

---

7. Expected Outcome

The expected outcome is a functional command-line Hangman game in which a player can:

1. Start the game.
2. Receive a randomly selected hidden word.
3. Guess letters one at a time.
4. See correctly guessed letters.
5. Track the number of wrong guesses.
6. View the progressive Hangman drawing.
7. Win by guessing the complete word.
8. Receive a Game Over message if all 6 wrong attempts are used.

---

8. Future Enhancements

The project can be further improved by adding:

- Difficulty levels such as Easy, Medium, and Hard.
- Categories such as Programming, Food, Animals, and Sports.
- A scoring system.
- Multiple rounds.
- A replay option.
- Hints for difficult words.
- A graphical user interface (GUI).
- A timer-based challenge.
- A high-score system.
- More advanced word selection and game statistics.

---

9. Conclusion

The Hangman Game is a simple Python-based project designed to demonstrate fundamental programming concepts through an interactive game. It combines random word selection, user input, string processing, loops, conditions, input validation, and game-state tracking.

The project provides a practical way to understand how basic Python concepts can be combined to create a complete working application.