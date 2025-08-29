import string
DIGITS = '0123456789'
ALLOWED = set(string.ascii_lowercase + DIGITS)
ATBASH = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])


def encode(text):
    s = text.lower()
    translated = s.translate(ATBASH)
    filtered = ''.join(ch for ch in translated if ch in ALLOWED)
    return ' '.join(filtered[i:i+5] for i in range(0,len(filtered),5))
    
        
def decode(ciphered_text):
    text = encode(ciphered_text).split(' ')
    return ''.join(text)    