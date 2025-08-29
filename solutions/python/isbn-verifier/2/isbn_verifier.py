def is_valid(isbn):
    s = isbn.replace('-','').replace(' ','').upper()
    if len(s) != 10: return False
    digits = list(s)
    if digits[-1] == 'X': digits[-1] = '10'
    total = 0
    for i,ch in enumerate(digits):
        if ch.isdigit():
            total += int(ch) * (10 - i)
        else: return False
    return (total % 11) == 0
        