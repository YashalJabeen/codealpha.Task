import random

def select_random_word():
    """Chooses a random word from a predefined list."""
    word_list = ["python", "programming", "hangman", "developer", "challenge"]
    return random.choice(word_list)

def reveal_correct_guesses(secret_word, guessed_chars):
    """Returns the word with correctly guessed letters revealed, and others as underscores."""
    return "".join(letter if letter in guessed_chars else "_" for letter in secret_word)

def play_hangman():
    """Runs the Hangman game where the user guesses letters of a random word."""
    secret_word = select_random_word()
    guessed_letters = set()
    remaining_attempts = 6  # Maximum incorrect guesses allowed

    print("Welcome to the Hangman Game!")

    while remaining_attempts > 0:
        print("\nWord:", reveal_correct_guesses(secret_word, guessed_letters))
        user_guess = input("Guess a letter: ").lower()

        if user_guess in guessed_letters:
            print("You've already guessed that letter! Try another.")
        elif user_guess in secret_word:
            guessed_letters.add(user_guess)
            print("Great! That letter is in the word.")
        else:
            guessed_letters.add(user_guess)
            remaining_attempts -= 1
            print(f"Oops! That letter is not in the word. Attempts left: {remaining_attempts}")

        # Check if the player has guessed the whole word
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You guessed the word: {secret_word}")
            return

    print(f"Game Over! The correct word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
