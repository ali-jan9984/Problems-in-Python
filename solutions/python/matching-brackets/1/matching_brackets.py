brackets = ['(', '{', '[']
matches = {')': '(', '}': '{', ']': '['}

def is_paired(input_string):
    if not input_string:
        return True
    stack = []
    for brc in input_string:
        if brc in brackets:
            stack.append(brc)
        if brc in matches:
            if not stack:
                return False
            if stack[-1] == matches[brc]:
                stack.pop()
            else:
                return False
    return True if not stack else False       