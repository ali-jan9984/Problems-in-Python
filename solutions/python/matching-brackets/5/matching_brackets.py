OPEN_BRACKETS = ['(','{','[']
CLOSE_BRACKETS = [')','}',']']


def is_paired(input_string):
    stack = []
    for bracket in input_string:
        if bracket in OPEN_BRACKETS:
            stack.append(bracket)
        if bracket in CLOSE_BRACKETS:
            if not stack or stack.pop() != OPEN_BRACKETS[CLOSE_BRACKETS.index(bracket)]:
                return False
    return not stack