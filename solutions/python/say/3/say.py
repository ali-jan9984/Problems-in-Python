ONES = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
TEENS = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
TENS = ("twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
SUFFIXES = ("", "thousand", "million", "billion")


def say(num: int) -> str:
    validate_range(num)
    if num == 0:
        return ONES[0]
    num_segments = []
    while num > 0:
        num_segments.append(num % 1000)
        num //= 1000
    words = []
    for suffix_index, segment in enumerate(num_segments):
        word_for_segment = convert_three_digit_group(segment)
        if suffix_index and word_for_segment:
            words.append(f"{word_for_segment} {SUFFIXES[suffix_index]}".strip())
        else:
            words.append(word_for_segment)
    return ' '.join(reversed(words)).strip()


def validate_range(num: int) -> None:
    if num < 0 or num > 999_999_999_999:
        raise ValueError("input out of range")
    

def convert_three_digit_group(num: int) -> str:
    str_num = str(num).zfill(3)
    hundreds_place, tens_place, ones_place = int(str_num[0]), int(str_num[1]), int(str_num[2])
    result = f"{ONES[hundreds_place]} hundred" if hundreds_place else ''
    if tens_ones:= format_tens_and_ones(tens_place,ones_place):
        result += f" {tens_ones}"
    return result    


def format_tens_and_ones(tens_place: int, ones_place: int) -> str:
    if tens_place > 1:
        tens_word = TENS[tens_place - 2]
        return f"{tens_word}-{ONES[ones_place]}" if ones_place else tens_word
    if tens_place == 1:
        return TEENS[ones_place]
    if ones_place > 0:
        return ONES[ones_place]
    return ''