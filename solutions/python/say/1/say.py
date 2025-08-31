ONES =('zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine')

TWOS =('ten',
       'eleven',
       'twelve',
       'thirteen',
       'fourteen',
       'fifteen',
       'sixteen',
       'seventeen',
       'eighteen',
       'nineteen')

TENS =('twenty',
       'thirty',
       'forty',
       'fifty',
       'sixty',
       'seventy',
       'eighty',
       'ninety',)

suffixes =('',
            'thousand',
            'million',
            'billion')


def say(number: int) -> str:
    if number < 0 or number > 999_999_999_999:
        raise ValueError('input out of range')
    if not number:
        return ONES[0]
    str_num = str(number)
    length = len(str_num)
    num_segments = []
    while length > 0:
        num_segments.append(str_num[max(0, length - 3):length])
        length -= 3
    words = []
    for idx, segment in enumerate(num_segments):
        word_segment = fetch_words(segment)
        if word_segment:
            words.append(word_segment + (' ' + suffixes[idx] if idx > 0 else '')) 
    return ' '.join(reversed(words)).strip()


def fetch_words(number: str) -> str:
    number = number.zfill(3)
    hundreds_place = int(number[0])
    tens_place = int(number[1])
    ones_place = int(number[2])
    words = []
    if hundreds_place > 0:
        words.append(ONES[hundreds_place])
        words.append('hundred')
    if tens_place > 1:
        if ones_place > 0:
            words.append(TENS[tens_place - 2] + '-' + ONES[ones_place])
        else:
            words.append(TENS[tens_place - 2])
    elif tens_place == 1:
        words.append(TWOS[ones_place])
    elif ones_place > 0:
        words.append(ONES[ones_place])
    return ' '.join(words)