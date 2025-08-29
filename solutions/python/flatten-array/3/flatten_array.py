def flatten(iterable):
    result = []
    for item in iterable:
        if item == None:
            continue
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
