BRACKETS = {')':'(','}':'{',']':'['}


def is_paired(input_string):
    stack = []
    open_brackets = set(BRACKETS.values())
    for bracket in input_string:
        if bracket in open_brackets:
            stack.append(bracket)
        if bracket in BRACKETS and (not stack or stack.pop() != BRACKETS[bracket]):
            return False
    return not stack