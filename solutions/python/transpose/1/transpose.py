def transpose(text):
    if not text:
        return ''
    rows = text.splitlines()
    ln = max(len(r) for r in rows)
    result = []
    for c in range(ln):
        col_chars = []
        for r in rows:
            if c < len(r):
                col_chars.append(r[c])
            else:
                col_chars.append('$')
        line = ''.join(col_chars).rstrip('$').replace('$', ' ')
        result.append(line)
    return "\n".join(result)