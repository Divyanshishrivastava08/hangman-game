import random

# List of words
words = [
    "python",
    "computer",
    "programming",
    "keyboard",
    "elephant",
    "guitar",
    "internet",
    "football",
    "string",
    "float",
    "boolean",
    "apple",
    "beautiful",
    "hangman",
    "drawing",
    "trust",
    "cricket",
    "lion",
    "developer",
    "coding",
    "computing",
    "argument",
    "array",
    "terminal",
    "CODE",
    "galaxy",
    "quiz",
    "axotic",
    "algorithm",
    "variable",
    "loop",
    "condition",
    "syntax",
    "exception",
    "debug",
    "object",
    "input",
    "output",
    "class",
    "method",
    "inheritance",
    "dizzy",
    "polymorphism",
    "encapsulation",
    "abstraction",
    "recursion",
    "stack",
    "queue",
    "dictionary",
    "list",
    "tuple",
    "set",
    "string",
    "integer",
    "rogue",
    "tounge",
    "step",
    "zombie",
    "memento",
    "pythonista",
    "games",
    "addive",
    "obnoxious",
    "sphinx",
    "xylophone",
    "juptyr",
    "flask",
    "django",
    "numpy",
    "pandas",
    "pemdas",
    "mango",
    "banana",
    "cheese",
    "chocolate",
    "burger",
    "pizza",
    "spaghetti",
    "sushi",
    "dumpling",
    "taco",
    "curry",
    "lasagna",
    "burrito",
    "chopsticks",
    "ramen",
    "morepan",
    "samosa",
    "kachori",
    "biryani",
    "noodles",
    "streak",
    "casserole",
    "swissroll",
    "pancake",
    "waffle",
    "croissant",
    "bagel",
    "pretzel"
]

# Choose a random word
word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Hangman drawings
hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


print("================================")
print("        H A N G M A N")
print("================================")
print("Guess the hidden word!")
print()

while wrong_guesses < max_wrong_guesses:

    # Display hangman
    print(hangman[wrong_guesses])

    # Display word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if player has won
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You won!")
        print("The word was:", word)
        break

    # Get player guess
    guess = input("\nGuess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

else:
    print(hangman[6])
    print("\n💀 Game Over!")
    print("The word was:", word)
