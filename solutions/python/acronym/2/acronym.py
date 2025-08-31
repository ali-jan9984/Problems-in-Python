import re


def abbreviate(words):
    return ''.join(word[0].upper() for word in re.findall(r"[a-zA-Z']+", words))