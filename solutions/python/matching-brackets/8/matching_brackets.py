BRACKETS = {')':'(','}':'{',']':'['}
OPEN_BRACKETS = set(BRACKETS.values())


def is_paired(input_string):
    stack = []
    for bracket in input_string:
        if bracket in OPEN_BRACKETS:
            stack.append(bracket)
        if bracket in BRACKETS and (not stack or stack.pop() != BRACKETS[bracket]):
            return False
    return not stack