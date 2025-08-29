import string
ALPHA = string.ascii_uppercase


def rows(letter):
    id = ALPHA.index(letter)
    letters = ALPHA[:id+1]
    rows = []
    for i,ch in enumerate(letters):
        if i == 0:
            row = ' ' * id + ch + ' ' * id
        else:
            row = ' ' * (id - i) + ch + ' ' * (2*i - 1) + ch + ' ' * (id - i)
        rows.append(row)
    rows += rows[-2::-1]
    return rows          