import re
RE = r"[^a-z0-9'\s]"


def count_words(sentence):
    sentence = sentence.lower()
    sentence = re.sub(RE, ' ', sentence)
    words = sentence.split()
    result = {}
    for word in words:
        key = word.replace("/", "").strip("'")
        if not key:
            continue
        result[key] = result.get(key, 0) + 1
    return result