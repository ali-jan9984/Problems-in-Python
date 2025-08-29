VOWELS = {'a','e','i','o','u'}
VOWELS_Y = {'a','e','i','o','u','y'}
SPECIAL = {'xr','yt'}

def translate(text):
    pig_latin = []
    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIAL:
            pig_latin.append(word + 'ay')
            continue
        for pos in range(1,len(word)):
            if word[pos] in VOWELS_Y:
                pos += 1 if word[pos] == 'u' and word[pos -1] == 'q' else 0
                pig_latin.append(word[pos:] + word[:pos] + 'ay')
                break
    return ' '.join(pig_latin)
        
    
    
