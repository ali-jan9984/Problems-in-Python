import itertools


def transpose(text):
    rows = text.splitlines()
    columns = itertools.zip_longest(*rows, fillvalue='~')
    lines = []

    for col in columns:
        joined = ''.join(col)
        trimmed = joined.rstrip('~')
        formatted = trimmed.replace('~', ' ')
        lines.append(formatted)
    
    return '\n'.join(lines)