def rotate(text, key):
    key = key % 26
    result = []
    for ch in text:
        if 'a'<= ch <='z' or 'A' <= ch <= 'Z':
            base = 'a' if ch.islower() else 'A'
            offset = ord(ch) - ord(base)
            new_offset = (offset + key) % 26
            new_ch = chr(ord(base) + new_offset)
            result.append(new_ch)
        else:
            result.append(ch)
    return "".join(result)
            
            
        
        
