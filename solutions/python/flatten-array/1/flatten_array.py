def flatten(iterable):
    result = []
    stack = list(iterable)
    while stack:
        item = stack.pop(0)
        if item is None:
            continue
        elif isinstance(item,list):
            stack = item + stack
        else:
            result.append(item)
    return result
