import random

from colorama import Fore, init


def get_wordlist(filename="nouns.txt") -> list[str]:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def choose_word(word_list: list[str]) -> str:
    return random.choice(word_list).upper()


def display_hangman(mistakes) -> None:
    states = [
        """
       -----
       |   |
           |
           |
           |
           |
    --------
    """,
        """
       -----
       |   |
       O   |
           |
           |
           |
    --------
    """,
        """
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    """,
        """
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    """,
        """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    --------
    """,
        """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    --------
    """,
        """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    --------
    """,
    ]
    print(states[min(mistakes, len(states) - 1)])


def display_game(word, guessed_letters: set, mistake_letters: set) -> None:
    displayed_word = [
        letter if letter in guessed_letters else "_" for letter in word]
    print(Fore.YELLOW + "Current word: " + " ".join(displayed_word))
    if len(mistake_letters) > 0:
        print(Fore.RED + "Mistakes: " + ", ".join(mistake_letters))
    display_hangman(len(mistake_letters))


def get_user_guess(guessed_letters: set, mistake_letters: set) -> str | None:
    guess = input(Fore.WHITE + "Guess a letter: ").upper()
    if len(guess) != 1 or not guess.isalpha() or not guess.isupper():
        print(Fore.CYAN + "Please enter a single uppercase letter.")
        return None
    elif guess in guessed_letters or guess in mistake_letters:
        print(Fore.CYAN + "You have already guessed that letter. Try another one.")
        return None
    return guess


def update_game_state(word, guess: str, guessed_letters: set, mistake_letters: set) -> None:
    if guess:
        if guess in word:
            guessed_letters.add(guess)
        else:
            mistake_letters.add(guess)


def game_loop(word: str) -> None:
    guessed_letters = set()
    mistake_letters = set()  
    max_errors = 6

    while len(mistake_letters) < max_errors and not set(word).issubset(guessed_letters):
        display_game(word, guessed_letters, mistake_letters)
        guess = get_user_guess(guessed_letters, mistake_letters)
        if guess:
            update_game_state(word, guess, guessed_letters, mistake_letters)

    if set(word).issubset(guessed_letters):
        print(Fore.GREEN + f"Congrats! You guessed the word: {word}")
    else:
        print(Fore.RED + f"You lost. The word was: {word}")



def menu() -> None:
    while True:
        choice = input(Fore.WHITE + "Press 'S' to start a new game or 'Q' to quit: ").upper()
        if choice == 'S':
            word_list = get_wordlist()
            word = choose_word(word_list)
            game_loop(word)
        elif choice == 'Q':
            print(Fore.CYAN + "Thanks for playing!")
            break
        else:
            print(Fore.CYAN + "Invalid choice. Please try again.")

def main() -> None:
    init(autoreset=True)
    print(Fore.CYAN + "Welcome to Hangman!")
    menu()

if __name__ == "__main__":
    main()