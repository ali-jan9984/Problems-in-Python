from collections import Counter
import re


def count_words(sentence):
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)*", sentence.lower())
    words = [word.strip("'") for word in words if word.strip("'")]
    return dict(Counter(words))
    