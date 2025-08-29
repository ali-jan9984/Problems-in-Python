def is_isogram(string):
    string = string.lower()
    list = []
    for ch in string:
        if ch in list and 'a'<= ch <= 'z':
            return False
        list.append(ch)
    return True
