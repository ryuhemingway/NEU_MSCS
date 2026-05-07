# hangman.py
# Team Members: Arja Sadhukhan, Saloni Surana, Ryu Hemingway
# NU ID <003163519>
# Course: CS 5001 / 5003 — Spring 2026

"""
Hangman Game with Matplotlib (HW9)

Built using an AI coding assistant as part of HW9.
The game lets two players play Hangman: one enters a secret word,
the other guesses letters while a matplotlib figure tracks wrong guesses.
"""

import matplotlib.pyplot as plt

MAX_WRONG = 6

# each lambda draws one body part: head, body, left arm, right arm, left leg, right leg
HANGMAN_PARTS = [
    lambda ax: ax.add_patch(plt.Circle((7, 7.5), 0.5, color="black", fill=False, linewidth=3)),  # head
    lambda ax: ax.plot([7, 7], [5, 7], color="black", linewidth=3),        # body
    lambda ax: ax.plot([7, 6], [6.5, 5.5], color="black", linewidth=3),    # left arm
    lambda ax: ax.plot([7, 8], [6.5, 5.5], color="black", linewidth=3),    # right arm
    lambda ax: ax.plot([7, 6], [5, 3.5], color="black", linewidth=3),      # left leg
    lambda ax: ax.plot([7, 8], [5, 3.5], color="black", linewidth=3),      # right leg
]


def render_gallows(ax):
    """
    Draws the static gallows structure (base, pole, beam, rope)
    onto the given axes.

    Parameters:
        ax (matplotlib.axes.Axes): The axes to draw on.
    """
    ax.plot([2, 8], [1, 1], color="black", linewidth=3)  # base
    ax.plot([5, 5], [1, 9], color="black", linewidth=3)  # pole
    ax.plot([5, 7], [9, 9], color="black", linewidth=3)  # beam
    ax.plot([7, 7], [9, 8], color="black", linewidth=3)  # rope


def update_figure(wrong_count):
    """
    Clears the figure and redraws the gallows plus any body parts
    earned by wrong guesses so far.

    Parameters:
        wrong_count (int): Number of incorrect guesses made.
    """
    plt.clf()                  # wipe the previous frame
    ax = plt.gca()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")             # hide the axis ticks and border
    ax.set_title(f"Wrong guesses: {wrong_count} / {MAX_WRONG}")

    render_gallows(ax)

    # draw one body part per wrong guess
    for i in range(wrong_count):
        HANGMAN_PARTS[i](ax)

    plt.pause(0.1)             # brief pause so the window refreshes


def build_display(word, guesses):
    """
    Returns the word with guessed letters revealed and underscores
    for letters not yet guessed.

    Parameters:
        word (str): The secret word.
        guesses (list): Letters guessed so far.

    Returns:
        str: The word with blanks, e.g. "h _ l l o".
    """
    return " ".join(ch if ch in guesses else "_" for ch in word)


def check_win(word, guesses):
    """
    Returns True if every letter in the word has been guessed.

    Parameters:
        word (str): The secret word.
        guesses (list): Letters guessed so far.

    Returns:
        bool: True if the player has revealed the full word.
    """
    return all(ch in guesses for ch in word)


def wrong_guesses(guesses, word):
    """
    Filters the guessed letters down to only the ones that are
    not in the secret word.

    Parameters:
        guesses (list): Letters guessed so far.
        word (str): The secret word.

    Returns:
        list: Incorrect guessed letters.
    """
    return [ch for ch in guesses if ch not in word]


def prompt_for_letter(guesses):
    """
    Asks the player for a single letter, re-prompting on invalid
    or duplicate input.

    Parameters:
        guesses (list): Letters already guessed (used to block repeats).

    Returns:
        str: A valid, new, single lowercase letter.
    """
    while True:
        letter = input("\nGuess a letter: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input. Enter exactly one letter.")
            continue

        if letter in guesses:
            print(f"You already guessed '{letter}'. Try a different letter.")
            continue

        return letter


def prompt_for_secret():
    """
    Asks Player 1 for the secret word, re-prompting until a valid
    alphabetic string is entered.

    Returns:
        str: The secret word in lowercase.
    """
    while True:
        word = input("Player 1, enter the secret word: ").strip()

        if word == "" or not word.isalpha():
            print("The word must be non-empty and contain only letters.")
            continue

        return word.lower()


def play_round(word):
    """
    Runs one complete round of Hangman for the given secret word.
    Handles the guess loop, display updates, and win/loss detection.

    Parameters:
        word (str): The secret word to guess.
    """
    guesses = []

    plt.ion()  # interactive mode so the window updates mid-game

    while True:
        misses = wrong_guesses(guesses, word)
        miss_count = len(misses)

        update_figure(miss_count)

        # show current game state in the terminal
        print(f"\nWord: {build_display(word, guesses)}")
        print(f"Remaining attempts: {MAX_WRONG - miss_count}")
        print(f"Missed letters: {', '.join(misses) if misses else 'none'}")

        # check end conditions before prompting for another guess
        if check_win(word, guesses):
            print(f"\nYou win! The word was: {word}")
            plt.ioff()
            plt.show()
            return

        if miss_count >= MAX_WRONG:
            print(f"\nYou lose! The word was: {word}")
            plt.ioff()
            plt.show()
            return

        guesses.append(prompt_for_letter(guesses))


def main():
    """
    Entry point. Handles the welcome banner, play-again loop,
    and passing the secret word into play_round.
    """
    while True:
        print("\n" + "=" * 40)
        print("       HANGMAN")
        print(f"  (max {MAX_WRONG} wrong guesses)")
        print("=" * 40)

        word = prompt_for_secret()
        print("\n" * 50)         # clear the screen so Player 2 can't see the word
        print("Player 2, your turn!\n")

        play_round(word)

        # ask if they want to go again
        again = input("\nPlay again? (yes/no): ").strip().lower()
        while again not in ("yes", "y", "no", "n"):
            again = input("Enter yes or no: ").strip().lower()

        if again in ("no", "n"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
