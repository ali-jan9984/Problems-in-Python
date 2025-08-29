def append(list1, list2):
    return [*list1, *list2]
def concat(lists):
    result = []
    for item in lists:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result
def filter(function, items):
    return [item for item in items if function(item)]
def length(list):
    return len(list)
def map(function, list):
    return [function(item) for item in list]
def foldl(function, lst, initial):
    acc = initial 
    for x in lst:
        acc = function(acc,x)
    return acc
def foldr(function, lst, initial):
    acc = initial
    for x in lst[::-1]:
        acc = function(acc,x)
    return acc
def reverse(items):
    return items[::-1]
