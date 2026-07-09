def line_up(name, number):
    ordSuffix = ""
    if (number % 100 == 11 or number % 100 == 12 or number % 100 == 13):
        ordSuffix = "th"
    else:
        if number % 10 == 1:
            ordSuffix = "st"
        elif number % 10 == 2:
            ordSuffix = "nd"
        elif number % 10 == 3:
            ordSuffix = "rd"
        else:
            ordSuffix = "th"
    return f"{name}, you are the {number}{ordSuffix} customer we serve today. Thank you!"