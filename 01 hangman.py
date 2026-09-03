import random

# Predefined list of words for the game
WORD_LIST = ["python", "computer", "keyboard", "monitor", "program"]

MAX_ATTEMPTS = 6


def display_banner():
    """Display a professional welcome banner for the game."""
    print("-" * 50)
    print("             WELCOME TO HANGMAN")
    print("           CodeAlpha Internship Project")
    print("-" * 50)
    print("Guess the hidden word one letter at a time.")
    print(f"You have {MAX_ATTEMPTS} incorrect attempts allowed.")
    print("**" * 50)


def choose_word():
    """Randomly select and return a word from the predefined word list."""
    return random.choice(WORD_LIST)


def display_word(word, guessed_letters):
    """
    Build and return the current state of the word to display,
    showing correctly guessed letters and underscores for the rest.
    """
    displayed_letters = []
    for letter in word:
        if letter in guessed_letters:
            displayed_letters.append(letter.upper())
        else:
            displayed_letters.append("_")
    return " ".join(displayed_letters)


def display_status(word, guessed_letters, wrong_attempts):
    """Display the current game status: word progress, wrong attempts,
    and letters already guessed."""
    print("-" * 50)
    print(f"Current Word: {display_word(word, guessed_letters)}")
    print(f"Wrong Attempts: {wrong_attempts}/{MAX_ATTEMPTS}")
    if guessed_letters:
        sorted_guesses = ", ".join(sorted(guessed_letters))
        print(f"Guessed Letters: {sorted_guesses}")
    else:
        print("Guessed Letters: None")
    print("-" * 50)


def get_guess(guessed_letters):
    """
    Prompt the user for a single alphabet letter, validate it,
    and ensure it has not already been guessed. Returns a valid,
    lowercase letter.
    """
    while True:
        guess = input("Enter your guess (a single letter): ").strip().lower()

        # Validate that exactly one character was entered
        if len(guess) != 1:
            print("Invalid input. Please enter exactly one letter.")
            continue

        # Validate that the character is an alphabet letter
        if not guess.isalpha():
            print("Invalid input. Please enter an alphabet letter only.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        return guess


def play_game():
    """Run a single round of the Hangman game."""
    word = choose_word()
    guessed_letters = set()
    wrong_attempts = 0

    print("\nA new word has been chosen. Let's begin!\n")

    while wrong_attempts < MAX_ATTEMPTS:
        display_status(word, guessed_letters, wrong_attempts)

        # Check win condition before asking for a new guess
        if all(letter in guessed_letters for letter in word):
            break

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_attempts += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check win condition immediately after the guess
        if all(letter in guessed_letters for letter in word):
            display_status(word, guessed_letters, wrong_attempts)
            print("\nCongratulations! You guessed the word correctly!")
            print(f"The word was: {word.upper()}")
            return

    # If the loop ended due to reaching max wrong attempts, player loses
    if wrong_attempts >= MAX_ATTEMPTS:
        print("\nGame Over! You have used all your attempts.")
        print(f"The correct word was: {word.upper()}")


def play_again():
    """
    Ask the player whether they want to play another round.
    Returns True if the player wants to continue, False otherwise.
    """
    while True:
        choice = input("\nDo you want to play again? (Y/N): ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


def main():
    """Main driver function to control the overall game loop."""
    display_banner()

    keep_playing = True
    while keep_playing:
        play_game()
        keep_playing = play_again()

    print("\n" + "=" * 50)
    print("Thank you for playing Hangman!")
    print("Have a great day!")
    print("**" * 50 )



main()