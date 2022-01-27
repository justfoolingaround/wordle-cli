import datetime
import pathlib
import random

import rich
import ujson

from .errors import MaxAttemptExceeded, NotFound, SizeNotAppropriate

with open(pathlib.Path(__file__).parent / f"assets/words.json", "r") as word_raw:
    words = ujson.load(word_raw)

with open(pathlib.Path(__file__).parent / f"assets/candidates.json", "r") as candidates_raw:
    candidates = ujson.load(candidates_raw)

all_words = candidates + words


class WordleClient():

    def __init__(self, word, all_words, *, max_attempt=6):
        self.word = word
        self.attempts = []

        self.max_attempt = max_attempt
        self.all_words = all_words

    @staticmethod
    def generate_matches(word, user_word):
        for actual, user_guess in zip(word, user_word):
            if actual == user_guess:
                yield (actual, True, True)
            else:
                if user_guess in word:
                    yield (user_guess, True, False)
                else:
                    yield (user_guess, False, False)

    def play(self, user_word):
        if self.attempt_count + 1 > self.max_attempt:
            raise MaxAttemptExceeded("Maximum attempts exceeded.")

        if len(user_word) != len(self.word):
            raise SizeNotAppropriate("{!r} is not of the selected word size {}.".format(user_word, len(self.word)))

        if user_word not in self.all_words:
            raise NotFound("{!r} was not found in the word list.".format(user_word))

        if user_word == self.word:
            return True

        attempt = list(self.generate_matches(self.word, user_word))
        self.attempts.append(attempt)

        return False

    def rich_print(self):
        for row in self.attempts:
            for word, in_word, exact_place in row:
                if in_word:
                    if exact_place:
                        rich.print("[green]{}[/]".format(word), end='')
                    else:
                        rich.print("[yellow]{}[/]".format(word), end='')
                else:
                    rich.print("[red]{}[/]".format(word), end='')
            rich.print()

    @property
    def attempt_count(self):
        return len(self.attempts)

    @classmethod
    def word_of_the_day(cls):
        return cls(candidates[(datetime.datetime.utcnow() - datetime.datetime(2022, 1, 1)).days % len(candidates)], all_words)

    @classmethod
    def random(cls):
        return cls(random.choice(candidates), all_words) 
