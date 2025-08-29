def flatten_lists(iterable):
    for item in iterable:
        if isinstance(item, list):
            yield from flatten_lists(item)
        elif item is not None:
            yield item

def flatten(iterable):
    return list(flatten_lists(iterable))
