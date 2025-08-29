MATCHES = {')': '(', '}': '{', ']': '['}
OPEN_BRACKETS = ['(','{','[']


def is_paired(input_string):
    stack = []
    for bracket in input_string:
        if bracket in OPEN_BRACKETS:
            stack.append(bracket)
        elif bracket in MATCHES:
            if not stack or (stack.pop() != MATCHES[bracket]):
                return False
        else:
            continue
    return not stack