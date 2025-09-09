from string import ascii_uppercase as letters
from random import shuffle
from itertools import product

letter_pairs = ("".join(p) for p in product(letters, letters))
number_pairs = (str(i).zfill(3) for i in range(1000))
name = [l + n for l, n in product(letter_pairs, number_pairs)]
shuffle(name)
ITERATOR = iter(name)


class Robot:
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = next(ITERATOR)