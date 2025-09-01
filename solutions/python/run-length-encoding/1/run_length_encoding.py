def decode(string):
    result = []
    numeric = ''
    for ch in string:
        if ch.isdigit():
            numeric += ch
        else:
            numeric = int(numeric) if numeric else 1
            result.append(ch*numeric)
            numeric = ''
    return ''.join(result)
    

def encode(string):
    result = []
    counter, repeat_ch = 0, None
    for ch in string:
        if repeat_ch is None: repeat_ch = ch
        if ch == repeat_ch: counter += 1
        else:
            result.append(f"{counter}{repeat_ch}") if counter > 1 else result.append(repeat_ch)
            counter = 1
            repeat_ch = ch
    if repeat_ch:
        result.append(f"{counter}{repeat_ch}") if counter > 1 else result.append(repeat_ch)
    return ''.join(result)