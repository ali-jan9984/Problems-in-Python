def square(number):
    if number <= 0 or number >= 65:
        raise ValueError("square must be between 1 and 64")
        return None
    else:
        return 2**(number-1)


def total():
    total = 0
    for num in range(1,65):
        total += square(num)
    return total
print(total())
