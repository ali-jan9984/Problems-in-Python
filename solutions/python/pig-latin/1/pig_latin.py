vowels = ['a','e','i','o','u','A','E','I','O','U']
def translate(text):
    def translate_word(word):
        if word[0] in vowels or word[:2] == 'xr' or word[:2] == 'yt':
            return word + 'ay'
        for i, ch in enumerate(word):
            if ch == 'u' and i > 0 and word[i-1] == 'q':
                return word[i+1:] + word[:i+1] + 'ay'
            if ch in vowels or (ch == 'y' and i > 0):
                return word[i:] + word[:i] + 'ay'
        return word  # fallback, shouldn't usually hit

    return " ".join(translate_word(w) for w in text.split())

