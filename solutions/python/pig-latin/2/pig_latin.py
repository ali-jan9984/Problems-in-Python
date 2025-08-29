import re
RE = re.compile('^(x(?!r)|y(?!t)|[^aeiouqxy]*(?:qu?)?)(.+)$')

def translate(phrase):
    return ' '.join(map(translate_word,phrase.split()))

def translate_word(word):
    m = RE.match(word)
    head,tail = m.groups()
    return tail + head + 'ay'
    
    
    
