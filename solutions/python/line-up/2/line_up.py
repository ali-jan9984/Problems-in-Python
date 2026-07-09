def line_up(name, number):
    ordinalNum = ""
    if (number % 100 == 11 or number % 100 == 12 or number % 100 == 13):
        ordinalNum = "th"
    else:
        if number % 10 == 1:
            ordinalNum = "st"
        elif number % 10 == 2:
            ordinalNum = "nd"
        elif number % 10 == 3:
            ordinalNum = "rd"
        else:
            ordinalNum = "th"
    return f"{name}, you are the {number}{ordinalNum} customer we serve today. Thank you!"