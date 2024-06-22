import random

from colorama import Fore


def get_random_word(word_list) -> str:
    return random.choice(word_list)


def display_hangman(stages, mistake_letters) -> None:
    print(stages[len(mistake_letters)])


def display_word(guessed_letters, word) -> None:
    display: str = "".join(
        [letter if letter in guessed_letters else "_" for letter in word]
    )
    print(Fore.CYAN + f"Word: {display}")


def display_mistakes(mistake_letters) -> None:
    if mistake_letters:
        mistakes: str = ", ".join(mistake_letters)
        print(Fore.RED + f"Mistakes: {mistakes}")


def get_guess() -> str | None:
    while True:
        guess: str = input(
            Fore.WHITE + "Guess a letter (or type 'exit' to quit): "
        ).lower()
        if guess == "exit":
            return None
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print(Fore.RED + "Please enter one letter.")


def is_guessed(guess: str, guessed_letters, mistake_letters) -> bool:
    if guess in guessed_letters or guess in mistake_letters:
        print(Fore.MAGENTA + f"You have already guessed: {guess}")
        return True
    else:
        return False


def handle_correct_guess(guess: str, guessed_letters, word) -> bool:
    guessed_letters.append(guess)
    if all(letter in guessed_letters for letter in word):
        display_word(guessed_letters, word)
        print(Fore.GREEN + f"Congrats! You guessed the word: {word}")
        return True
    return False


def handle_incorrect_guess(
    guess: str,
    mistake_letters,
    word,
    max_errors,
    stages,
) -> bool:
    mistake_letters.append(guess)
    if len(mistake_letters) >= max_errors:
        display_hangman(mistake_letters, stages)
        print(Fore.RED + f"You died. The word was: {word}")
        return True
    return False


def play_again() -> bool:
    choice: str = input(Fore.WHITE + "Would you like to play again? (y/n) ").lower()
    return choice == "y"


def launch(stages, word_list) -> None:
    while True:
        print(Fore.GREEN + "Hello! Welcome to Hangman!")
        choice: str = input(
            Fore.WHITE + 'Enter "y" to start a new game or "n" for exit: '
        ).lower()
        if choice == "y":
            start_game(stages, word_list)
        elif choice == "n":
            print(Fore.CYAN + "Thanks for playing!")
            break
        else:
            print(Fore.RED + 'Please enter either "y" or "n".')


def start_game(stages, word_list) -> None:
    word = get_random_word(word_list)
    guessed_letters = []
    mistake_letters = []
    game_over = False
    max_errors: int = len(stages) - 1

    while not game_over:
        display_hangman(stages, mistake_letters)
        display_word(guessed_letters, word)
        display_mistakes(mistake_letters)

        guess = get_guess()
        if guess is None:
            break

        if is_guessed(guess, guessed_letters, mistake_letters):
            continue

        if guess in word:
            game_over = handle_correct_guess(guess, guessed_letters, word)
        else:
            game_over = handle_incorrect_guess(
                guess, mistake_letters, word, max_errors, stages
            )

    if play_again():
        start_game(stages, word_list)
    else:
        print(Fore.CYAN + "Thanks for playing!")
