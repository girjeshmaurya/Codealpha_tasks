"""CodeAlpha Python Internship - Task 1: Hangman Game"""
import random

WORDS = ["python", "internship", "variable", "function", "keyboard"]
MAX_WRONG = 6

STAGES = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
]


def show_state(word, guessed, wrong):
    print(STAGES[len(wrong)])
    print("\nWord:", " ".join(c if c in guessed else "_" for c in word))
    print("Wrong guesses:", ", ".join(sorted(wrong)) or "none")
    print(f"Attempts left: {MAX_WRONG - len(wrong)}\n")


def play():
    word = random.choice(WORDS)
    guessed, wrong = set(), set()

    print("=== HANGMAN ===")
    while len(wrong) < MAX_WRONG:
        show_state(word, guessed, wrong)

        if all(c in guessed for c in word):
            print(f"You won! The word was '{word}'.")
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed or guess in wrong:
            print("You already guessed that letter.")
        elif guess in word:
            guessed.add(guess)
            print("Good guess!")
        else:
            wrong.add(guess)
            print("Wrong guess!")

    show_state(word, guessed, wrong)
    print(f"Game over! The word was '{word}'.")


def main():
    while True:
        play()
        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
