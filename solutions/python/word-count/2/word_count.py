import re
RE = r"[^a-z0-9'\s]"


def count_words(sentence):
    sentence = sentence.lower()
    sentence = re.sub(RE, ' ', sentence)
    list_of_words = sentence.split()
    result = {}
    for word in list_of_words:
        key = word.replace("/", "").strip("'")
        if not key:
            continue
        result[key] = result.get(key, 0) + 1
    return result