def egg_count(display_value):
    spots = [0,0]
    quotient = display_value
    reminder = 0
    while quotient != 0:
        reminder = quotient % 2
        quotient = quotient // 2
        spots[reminder] += 1
    return spots[1]