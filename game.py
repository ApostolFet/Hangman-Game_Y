import random
from colorama import Fore, init

init(autoreset=True)

class Hangman:
    def __init__(self, word_list: list[str], stages: list[str]) -> None:
        self.word_list: list[str] = word_list
        self.stages: list[str] = stages
        self.word: str = ""
        self.guessed_letters: list[str] = []
        self.mistake_letters: list[str] = []
        self.max_errors: int = len(stages) - 1
        self.game_over: bool = False

    def get_random_word(self) -> str:
        return random.choice(self.word_list)

    def display_hangman(self) -> None:
        print(self.stages[len(self.mistake_letters)])

    def display_word(self) -> None:
        display: str = "".join(
            [letter if letter in self.guessed_letters else "_" for letter in self.word]
        )
        print(Fore.CYAN + f"Word: {display}")

    def display_mistakes(self) -> None:
        if self.mistake_letters:
            mistakes: str = ", ".join(self.mistake_letters)
            print(Fore.RED + f"Mistakes: {mistakes}")

    def get_guess(self) -> str:
        while True:
            guess: str = input(Fore.WHITE + "Guess a letter (or type 'exit' to quit): ").lower()
            if guess == 'exit':
                self.game_over = True
                return ''
            if len(guess) == 1 and guess.isalpha():
                return guess
            else:
                print(Fore.RED + "Please enter one letter.")

    def is_guessed(self, guess: str) -> bool:
        if guess in self.guessed_letters or guess in self.mistake_letters:
            print(Fore.MAGENTA + f"You have already guessed: {guess}")
            return True
        else:
            return False

    def handle_correct_guess(self, guess: str) -> None:
        self.guessed_letters.append(guess)
        if all(letter in self.guessed_letters for letter in self.word):
            self.display_word()
            print(Fore.GREEN + f"Congrats! You guessed the word: {self.word}")
            self.game_over = True

    def handle_incorrect_guess(self, guess: str) -> None:
        self.mistake_letters.append(guess)
        if len(self.mistake_letters) >= self.max_errors:
            self.display_hangman()
            print(Fore.RED + f"You died. The word was: {self.word}")
            self.game_over = True

    def play_again(self) -> bool:
        choice: str = input(Fore.WHITE + "Would you like to play again? (y/n) ").lower()
        return choice == "y"

    def launch(self) -> None:
        while True:
            print(Fore.GREEN + "Hello! Welcome to Hangman!")
            choice: str = input(
                Fore.WHITE + 'Enter "y" to start a new game or "n" for exit: '
            ).lower()
            if choice == "y":
                self.start_game()
            elif choice == "n":
                print(Fore.CYAN + "Thanks for playing!")
                break
            else:
                print(Fore.RED + 'Please enter either "y" or "n".')

    def start_game(self) -> None:
        self.word = self.get_random_word()
        self.guessed_letters = []
        self.mistake_letters = []
        self.game_over = False

        while not self.game_over:
            self.display_hangman()
            self.display_word()
            self.display_mistakes()

            guess: str = self.get_guess()
            if self.game_over:  
                break

            if self.is_guessed(guess):
                continue

            if guess in self.word:
                self.handle_correct_guess(guess)
            else:
                self.handle_incorrect_guess(guess)

        if self.play_again():
            self.start_game()
        else:
            print(Fore.CYAN + "Thanks for playing!")
