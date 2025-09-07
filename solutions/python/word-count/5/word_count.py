from collections import Counter
from re import findall


def count_words(sentence):
    words = findall(r"[a-z0-9]+(?:'[a-z0-9]+)*", sentence.lower())
    return dict(Counter(words))
    