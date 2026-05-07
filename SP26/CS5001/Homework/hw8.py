# hangman.py
# Team Members: Arja Sadhukhan, Saloni Surana, Ryu Hemingway
# NU ID(s): <ID 1>, <ID 2>, <003163519>
# Course: CS 5001 / 5003 — Spring 2026

"""
Hangman Game with Matplotlib

For our HW8 assignment, we are tasked to chnage our program from playing the Hangman game in terminal to a matplotlib style. 
"""

import matplotlib.pyplot as plt

MAX_WRONG = 6

# Enable interactive mode so the window stays open during the game loop
plt.ion()


def draw_hangman(wrong_count):
    """
    Draws the hangman figure based on the number of wrong guesses (0-6).
    Clears and redraws each time so the window stays up to date.s
    """
    plt.clf()
    ax = plt.gca()

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f'Wrong guesses: {wrong_count}')

    # gallows
    ax.plot([2, 8], [1, 1], color='black', linewidth=3)  # base
    ax.plot([5, 5], [1, 9], color='black', linewidth=3)  # pole
    ax.plot([5, 7], [9, 9], color='black', linewidth=3)  # beam
    ax.plot([7, 7], [9, 8], color='black', linewidth=3)  # rope

    if wrong_count >= 1:
        head = plt.Circle((7, 7.5), 0.5, color='black', fill=False, linewidth=3)
        ax.add_patch(head)

    if wrong_count >= 2:
        ax.plot([7, 7], [5, 7], color='black', linewidth=3)  # body

    if wrong_count >= 3:
        ax.plot([7, 6], [6.5, 5.5], color='black', linewidth=3)  # left arm

    if wrong_count >= 4:
        ax.plot([7, 8], [6.5, 5.5], color='black', linewidth=3)  # right arm

    if wrong_count >= 5:
        ax.plot([7, 6], [5, 3.5], color='black', linewidth=3)  # left leg

    if wrong_count >= 6:
        ax.plot([7, 8], [5, 3.5], color='black', linewidth=3)  # right leg


def get_display_word(secret_word, guessed_letters):
    """
    Returns the word with guessed letters revealed and underscores
    for letters not yet guessed.

    Parameters:
        secret_word (str): The secret word.
        guessed_letters (list): Letters guessed so far

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


def play_hangman(secret_word):
    """
    Runs one full game of Hangman for the given secret word.

    Parameters:
        secret_word (str): The word to guess.
    """
    secret_word = secret_word.lower()
    guessed_letters = []

    while True:
        wrong_letters = get_wrong_guesses(guessed_letters, secret_word)
        wrong_count = len(wrong_letters)

        draw_hangman(wrong_count)
        plt.pause(0.1)

        print(f"\nWord: {get_display_word(secret_word, guessed_letters)}")
        print(f"Wrong guesses remaining: {MAX_WRONG - wrong_count}")

        if wrong_letters:
            print(f"Wrong guesses: {', '.join(wrong_letters)}")
        else:
            print("Wrong guesses: none")

        if is_won(secret_word, guessed_letters):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            draw_hangman(wrong_count)
            plt.ioff()
            plt.show()
            break

        if is_lost(wrong_count, MAX_WRONG):
            print(f"\nGame over. You ran out of guesses. The word was: {secret_word}")
            draw_hangman(MAX_WRONG)
            plt.ioff()
            plt.show()
            break

        while True:
            guess = input("\nEnter a letter: ").strip().lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter exactly one letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter. Try another one.")
                continue

            break

        guessed_letters.append(guess)


if __name__ == "__main__":
    while True:
        print("\n" + "=" * 40)
        print("Welcome to Hangman!")
        print(f"You can make at most {MAX_WRONG} wrong guesses.")
        print("=" * 40 + "\n")

        secret_word = input("Player 1, enter the secret word: ").strip()

        while len(secret_word) == 0 or not secret_word.isalpha():
            print("The secret word must contain letters only and cannot be empty.")
            secret_word = input("Player 1, enter the secret word: ").strip()

        print("\n" * 50)
        print("Player 2, it's your turn!")

        play_hangman(secret_word)

        print()
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()

        while play_again not in ["yes", "y", "no", "n"]:
            play_again = input("Please enter yes or no: ").strip().lower()

        if play_again in ["no", "n"]:
            print("Thanks for playing Hangman. Goodbye!")
            break