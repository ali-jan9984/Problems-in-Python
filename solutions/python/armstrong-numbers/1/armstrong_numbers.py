def is_armstrong_number(number):
    if number >=0:
        digit = [int(d) for d in str(number)]
        length = len(digit)
        total = 0
        for dig in digit:
            total += dig**length
        if total == number:
            return True
        else:
            return False
    return False
print(is_armstrong_number(153))
            
