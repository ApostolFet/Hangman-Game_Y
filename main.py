from colorama import init

from constants import STAGES
from game import launch


def get_wordlist() -> list[str]:
    with open("nouns.txt", "r", encoding="utf-8") as f:
        return f.read().splitlines()


def main() -> None:
    init(autoreset=True)
    word_list: list[str] = get_wordlist()
    launch(STAGES, word_list)


if __name__ == "__main__":
    main()
