🎮 Hangman Game in Python

📌 Project Overview

Hangman Game is a beginner-friendly, terminal-based word guessing game developed using Python.

The player has to guess a randomly selected word by entering one letter at a time. For every incorrect guess, a part of the Hangman figure is displayed. The player wins by guessing all the letters of the word before using all available chances.

This project demonstrates basic Python programming concepts such as variables, lists, loops, conditional statements, functions, modules, input validation, random selection, and exception/error handling.

---

🎯 Objectives

The main objectives of this project are:

- To develop a simple and interactive word guessing game.
- To apply basic Python programming concepts in a practical project.
- To implement user input validation.
- To provide a clear and user-friendly terminal interface.
- To organize the project into separate Python modules.
- To practice testing and GitHub-based version control.

---

✨ Features

- 🎲 Random word selection.
- 🎮 Interactive terminal-based gameplay.
- 🔤 Letter-by-letter word guessing.
- ❤️ Limited number of chances.
- 🪢 ASCII Hangman drawing.
- 📝 Display of guessed letters.
- ✅ Correct guess notification.
- ❌ Wrong guess notification.
- ⚠️ Detection of repeated guesses.
- 🚫 Input validation.
- 🏆 Win and Game Over conditions.
- 📊 Score calculation.
- 🔄 Replay option.
- 😊 Simple and beginner-friendly interface.

---

🛠️ Technologies and Tools

Technology/Tool| Purpose
Python 3| Main programming language
VS Code| Code development and execution
Git| Version control
GitHub| Source code management and project hosting
Python "random" module| Random word selection
Python "unittest"| Testing

---

💻 System Requirements

Hardware Requirements

- Any computer or laptop.
- Minimum 2 GB RAM.
- Basic keyboard and display.

Software Requirements

- Python 3.x
- VS Code or any Python-compatible IDE.
- Git and GitHub account (for version control).

---

📂 Project Structure

Hangman-Game/
│
├── main.py
├── game.py
├── words.py
├── display.py
├── validation.py
├── score.py
│
├── tests/
│   └── test_validation.py
│
├── README.md
├── statement.md
├── diagrams.md
├── project_report.md
└── requirements.txt

---

📖 Description of Files

"main.py"

The main entry point of the project. It starts the Hangman game and controls the overall program flow.

"game.py"

Contains the main game logic, including word selection, guessing, attempts, win condition, and game-over condition.

"words.py"

Contains the list of words used in the game.

"display.py"

Handles the display of the Hangman drawing and game information.

"validation.py"

Validates user input and checks whether the entered guess is valid.

"score.py"

Handles the score calculation used by the game.

"tests/test_validation.py"

Contains unit tests for checking input validation functionality.

---

⚙️ Installation

Step 1: Install Python

Download and install Python 3 from the official Python website.

Make sure Python is added to the system PATH during installation.

Step 2: Clone the Repository

Open the terminal and run:

git clone <your-github-repository-link>

Step 3: Open the Project

Move into the project folder:

cd Hangman-Game

Step 4: Run the Game

Execute:

python main.py

If your system uses "python3", use:

python3 main.py

---

🎮 How to Play

1. Start the program.
2. A random word is selected by the game.
3. The hidden word is displayed using underscores.
4. Enter one letter at a time.
5. If the letter is correct, it is revealed in the word.
6. If the letter is incorrect, one chance is lost.
7. Previously guessed letters are not accepted again.
8. Continue guessing until:
   - All letters are correctly guessed → You Win 🎉
   - All chances are used → Game Over 💀

---

🖥️ Example

================================
       🎮 HANGMAN GAME 🎮
================================

Word: _ _ _ _ _ _
Guessed letters: None
❤️ Chances left: 6

Enter a letter: p

✅ Correct guess!

Word: P _ _ _ _ _

---

📥 Input

The game accepts:

- One alphabetic character at a time.
- Lowercase or uppercase letters.
- User guesses entered through the keyboard.

Invalid Inputs

The program rejects:

- Numbers.
- Special characters.
- Empty input.
- More than one character.
- Previously entered letters.

Example:

Enter a letter: 5

❌ Please enter one letter.

---

📤 Output

The program displays:

- Current Hangman drawing.
- Hidden or revealed letters of the word.
- Previously guessed letters.
- Remaining chances.
- Correct/wrong guess messages.
- Final score.
- Win or Game Over message.

---

🧩 Functional Modules

The project contains the following major functional modules:

1. Game Controller

Controls the overall game flow and connects different modules.

2. Word Management

Stores and randomly selects words for the game.

3. Display Management

Displays the Hangman figure, word progress, guesses, and game messages.

4. Input Validation

Checks whether the player's input is valid.

5. Score Management

Calculates and manages the player's score.

---

🔄 Game Workflow

Start
  ↓
Select Random Word
  ↓
Display Hidden Word
  ↓
Ask Player for a Letter
  ↓
Validate Input
  ↓
Is Letter Already Guessed?
  ├── Yes → Show Warning → Ask Again
  └── No
       ↓
   Check Letter
       ↓
   ┌───────────────┐
   │               │
 Correct         Wrong
   │               │
   ↓               ↓
Reveal Letter   Lose Chance
   │               │
   └───────┬───────┘
           ↓
   Word Completely Guessed?
      ├── Yes → You Win 🎉
      └── No
           ↓
   Chances Remaining?
      ├── Yes → Continue Game
      └── No → Game Over 💀

---

🧪 Testing

The project includes basic testing for input validation.

Test Cases

Test Case| Input| Expected Result
Valid letter| "a"| Accepted
Uppercase letter| "A"| Accepted
Number| "5"| Rejected
Special character| "@"| Rejected
Multiple characters| "abc"| Rejected
Empty input| Empty| Rejected
Repeated letter| Previously guessed letter| Warning displayed

Run Tests

From the project directory, run:

python -m unittest discover

---

🛡️ Error Handling

The project handles common user input errors such as:

- Invalid characters.
- Multiple-character input.
- Empty input.
- Repeated guesses.

The program displays suitable messages instead of stopping unexpectedly.

---

⚡ Non-Functional Requirements

Usability

The game provides a simple terminal interface that is easy for beginners to understand.

Performance

The program uses simple Python operations and requires very few system resources.

Reliability

The game validates user input and handles common input errors.

Maintainability

The project is divided into multiple modules so that different parts of the program can be modified independently.

Resource Efficiency

The game does not require external databases or heavy software resources.

Error Handling

Invalid inputs are checked before they are processed by the game.

---

🧠 Python Concepts Used

This project demonstrates:

- Variables
- Data types
- Lists
- Strings
- "if-else" statements
- "for" loops
- "while" loops
- Functions
- Modules
- Import statements
- Random word selection
- User input
- Input validation
- Exception/error handling
- Unit testing

---

🔮 Future Enhancements

The project can be improved in the future by adding:

- Different difficulty levels.
- Larger word categories.
- Hint system.
- Timer-based gameplay.
- High-score system.
- Multiplayer mode.
- Graphical user interface (GUI).
- Database-based score storage.
- More word categories.
- Sound effects and animations.

---

📸 Screenshots

Screenshots of the running game can be added here.

Example:

![Game Screenshot](screenshots/game.png)

---

👩‍💻 Author

Divyanshi Shrivastava

CSE Core

---

📄 Project Documentation

Additional project documentation is available in:

- "statement.md" – Problem statement, scope, target users, requirements and features.
- "diagrams.md" – System architecture and design diagrams.
- "project_report.md" – Detailed project report.

---

📜 License

This project is created for educational and academic purposes.