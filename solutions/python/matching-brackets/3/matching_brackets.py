matches = {')': '(', '}': '{', ']': '['}

def is_paired(input_string):
    stack = []
    for brc in input_string:
        if brc in matches.values():
            stack.append(brc)
        elif brc in matches:
            if not stack or (stack.pop() != matches[brc]):
                return False
        else:
            continue
    return not stack