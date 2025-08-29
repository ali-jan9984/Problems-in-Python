matches = {')': '(', '}': '{', ']': '['}

def is_paired(input_string):
    stack = []
    for brc in input_string:
        if brc in matches.values():
            stack.append(brc)
        elif brc in matches:
            if not stack:
                return False
            if stack[-1] == matches[brc]:
                stack.pop()
            else:
                return False
        else:
            continue
    return True if not stack else False