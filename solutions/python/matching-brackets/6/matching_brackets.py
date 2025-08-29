BRACKETS = {')':'(','}':'{',']':'['}


def is_paired(input_string):
    stack = []
    for bracket in input_string:
        if bracket in BRACKETS.values():
            stack.append(bracket)
        if bracket in BRACKETS and (not stack or stack.pop() != BRACKETS[bracket]):
            return False
    return not stack