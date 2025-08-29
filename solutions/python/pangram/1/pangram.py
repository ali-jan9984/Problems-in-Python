def is_pangram(sentence):
    sentence = sentence.lower()
    letters = {ch for ch in sentence if 'a'<= ch <= 'z'}
    return len(letters) == 26
