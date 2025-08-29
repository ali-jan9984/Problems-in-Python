def append(list1, list2):
    return list1 + list2
def concat(lists):
    flatten_list = []
    for item in lists:
        for value in item:
            flatten_list.append(value)
    return flatten_list
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
