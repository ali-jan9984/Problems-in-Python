def is_valid(isbn):
    s = isbn.replace('-','').replace(' ','').upper()
    if not len(s) == 10:
        return False
    total = 0
    for i,ch in enumerate(s):
        weight = 10 - i
        if (ch.isdigit()) or (ch == 'X' and i == len(s) -1):
            digit = 10 if ch == 'X' else int(ch)
            total += digit * weight
        else:
            return False
    return (total % 11) == 0
        