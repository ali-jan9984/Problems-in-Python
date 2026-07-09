def line_up(name, number):
    ordinalSuffix = ""
    if (number % 100 == 11 or number % 100 == 12 or number % 100 == 13):
        ordinalSuffix = "th"
    else:
        if number % 10 == 1:
            ordinalSuffix = "st"
        elif number % 10 == 2:
            ordinalSuffix = "nd"
        elif number % 10 == 3:
            ordinalSuffix = "rd"
        else:
            ordinalSuffix = "th"
    return f"{name}, you are the {number}{ordinalSuffix} customer we serve today. Thank you!"