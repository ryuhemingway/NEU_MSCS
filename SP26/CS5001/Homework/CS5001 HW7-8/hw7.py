# hangman.py
# Team Members: Arja Sadhukhan, Saloni Surana, Ryu Hemingway
# NU ID(s): <ID 1>, <ID 2>, <ID 3>
# Course: CS 5001 / 5003 — Spring 2026

"""
Hangman Game

This program implements a terminal-based Hangman game.
It follows the assignment requirements:
1. Uses helper functions
2. Includes docstrings
3. Includes example calls in comments
4. Uses a main game loop
5. Supports replay

Extra features added:
- Colours
- Changing themes
- Optional sound
- Hidden secret word input for Player 1
"""

import os
import time
from getpass import getpass

MAX_WRONG = 6
USE_COLOURS = True
USE_SOUND = False   # Set to True only if terminal bell works on your machine

THEMES = [
    {
        "name": "Forest",
        "title": "\033[92m",
        "text": "\033[32m",
        "good": "\033[96m",
        "bad": "\033[91m",
        "warn": "\033[93m",
        "reset": "\033[0m"
    },
    {
        "name": "Ocean",
        "title": "\033[94m",
        "text": "\033[36m",
        "good": "\033[92m",
        "bad": "\033[95m",
        "warn": "\033[93m",
        "reset": "\033[0m"
    },
    {
        "name": "Sunset",
        "title": "\033[95m",
        "text": "\033[33m",
        "good": "\033[92m",
        "bad": "\033[91m",
        "warn": "\033[96m",
        "reset": "\033[0m"
    }
]


def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_theme(game_number):
    """
    Returns a theme dictionary based on the game number.

    Parameters:
        game_number (int): Current game number.

    Returns:
        dict: Selected theme settings.
    """
    return THEMES[(game_number - 1) % len(THEMES)]


def colour_text(text, colour_code, theme):
    """
    Wraps text in colour codes if colours are enabled.

    Parameters:
        text (str): The text to display.
        colour_code (str): ANSI colour code.
        theme (dict): Current theme dictionary.

    Returns:
        str: Coloured text if enabled, otherwise plain text.
    """
    if USE_COLOURS:
        return f"{colour_code}{text}{theme['reset']}"
    return text


def play_sound():
    """
    Plays a simple terminal bell sound if enabled.

    Note:
        This may not work in every VS Code terminal setup.
    """
    if USE_SOUND:
        print("\a", end="")


def display_hangman(wrong_count, theme):
    """
    Displays the hangman drawing based on the number of wrong guesses.

    Parameters:
        wrong_count (int): Number of wrong guesses made.
        theme (dict): Current theme dictionary.
    """
    stages = [
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

    print(colour_text(stages[wrong_count], theme["warn"], theme))


def get_display_word(secret_word, guessed_letters):
    """
    Returns a string showing guessed letters in their correct positions
    and underscores for letters not yet guessed. Letters are separated by spaces.

    Parameters:
        secret_word (str): The secret word.
        guessed_letters (list): Letters guessed so far.

    Returns:
        str: Current display version of the word.
    """
    display_letters = []

    for letter in secret_word:
        if letter in guessed_letters:
            display_letters.append(letter)
        else:
            display_letters.append("_")

    return " ".join(display_letters)


# Example calls:
# print(get_display_word('elephant', ['e', 'l', 'a']))   # e l e _ _ a _ _
# print(get_display_word('cat', []))                     # _ _ _


def is_won(secret_word, guessed_letters):
    """
    Returns True if every letter in the secret word has been guessed.

    Parameters:
        secret_word (str): The secret word.
        guessed_letters (list): Letters guessed so far.

    Returns:
        bool: True if player has guessed the word, False otherwise.
    """
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


# Example calls:
# print(is_won('cat', ['c', 'a', 't']))   # True
# print(is_won('cat', ['c', 'a']))        # False


def is_lost(wrong_count, max_wrong):
    """
    Returns True if wrong guesses have reached or exceeded the maximum allowed.

    Parameters:
        wrong_count (int): Number of wrong guesses made.
        max_wrong (int): Maximum wrong guesses allowed.

    Returns:
        bool: True if player has lost, False otherwise.
    """
    return wrong_count >= max_wrong


# Example calls:
# print(is_lost(6, 6))   # True
# print(is_lost(4, 6))   # False


def get_wrong_guesses(guessed_letters, secret_word):
    """
    Returns a list of guessed letters that are not in the secret word.

    Parameters:
        guessed_letters (list): Letters guessed so far.
        secret_word (str): The secret word.

    Returns:
        list: List of incorrect guessed letters.
    """
    wrong_letters = []

    for letter in guessed_letters:
        if letter not in secret_word:
            wrong_letters.append(letter)

    return wrong_letters


# Example calls:
# print(get_wrong_guesses(['e', 'z', 'l', 'q'], 'elephant'))   # ['z', 'q']
# print(get_wrong_guesses(['a', 'b'], 'apple'))                # ['b']


def get_hidden_secret_word(prompt_text):
    """
    Gets the secret word from Player 1 while hiding the actual letters.

    It tries to show asterisks (*) while typing if the Python version supports it.
    Otherwise, it falls back to fully hidden input.

    Parameters:
        prompt_text (str): Prompt shown to Player 1.

    Returns:
        str: The entered secret word in lowercase with surrounding spaces removed.
    """
    try:
        return getpass(prompt_text, echo_char="*").strip().lower()
    except TypeError:
        return getpass(prompt_text).strip().lower()


def play_hangman(secret_word, game_number=1):
    """
    Runs one full game of Hangman for the given secret word.

    Parameters:
        secret_word (str): The word to guess.
        game_number (int): Current game number, used for theme rotation.
    """
    secret_word = secret_word.lower()
    guessed_letters = []
    theme = get_theme(game_number)

    while True:
        wrong_letters = get_wrong_guesses(guessed_letters, secret_word)
        wrong_count = len(wrong_letters)

        clear_screen()

        print(colour_text("=" * 50, theme["title"], theme))
        print(colour_text(f"Hangman Theme: {theme['name']}", theme["title"], theme))
        print(colour_text("=" * 50, theme["title"], theme))

        display_hangman(wrong_count, theme)

        print(colour_text(f"Word: {get_display_word(secret_word, guessed_letters)}", theme["text"], theme))
        print(colour_text(f"Wrong guesses remaining: {MAX_WRONG - wrong_count}", theme["text"], theme))

        if wrong_letters:
            print(colour_text(f"Wrong guesses: {', '.join(wrong_letters)}", theme["bad"], theme))
        else:
            print(colour_text("Wrong guesses: none", theme["text"], theme))

        if is_won(secret_word, guessed_letters):
            print()
            print(colour_text(f"Congratulations! You guessed the word: {secret_word}", theme["good"], theme))
            play_sound()
            break

        if is_lost(wrong_count, MAX_WRONG):
            print()
            print(colour_text(f"Game over. You ran out of guesses. The word was: {secret_word}", theme["bad"], theme))
            play_sound()
            break

        print()

        while True:
            guess = input("Enter a letter: ").strip().lower()

            if len(guess) != 1:
                print(colour_text("Please enter exactly one character.", theme["warn"], theme))
                continue

            if not guess.isalpha():
                print(colour_text("Please enter a letter only.", theme["warn"], theme))
                continue

            if guess in guessed_letters:
                print(colour_text("You already guessed that letter. Try another one.", theme["warn"], theme))
                continue

            break

        guessed_letters.append(guess)

        if guess in secret_word:
            print(colour_text(f"Good guess! '{guess}' is in the word.", theme["good"], theme))
        else:
            print(colour_text(f"'{guess}' is not in the word.", theme["bad"], theme))
            play_sound()

        time.sleep(1.2)


if __name__ == "__main__":
    game_number = 1

    while True:
        clear_screen()
        print("Welcome to Hangman!")
        print("Player 1 enters a secret word.")
        print("Player 2 guesses one letter at a time.")
        print(f"You can make at most {MAX_WRONG} wrong guesses.")
        print()

        secret_word = get_hidden_secret_word("Player 1, enter the secret word: ")

        while len(secret_word) == 0 or not secret_word.isalpha():
            print("The secret word must contain letters only and cannot be empty.")
            secret_word = get_hidden_secret_word("Player 1, enter the secret word: ")

        clear_screen()
        print("Player 2, it's your turn!")
        time.sleep(1)

        play_hangman(secret_word, game_number)

        print()
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()

        while play_again not in ["yes", "y", "no", "n"]:
            play_again = input("Please enter yes or no: ").strip().lower()

        if play_again in ["no", "n"]:
            print("Thanks for playing Hangman. Goodbye!")
            break
            
        game_number += 1
