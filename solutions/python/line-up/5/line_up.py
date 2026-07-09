def line_up(name, number):
    ord_suffix = ""
    if (number % 100 == 11 or number % 100 == 12 or number % 100 == 13):
        ord_suffix = "th"
    else:
        if number % 10 == 1:
            ord_suffix = "st"
        elif number % 10 == 2:
            ord_suffix = "nd"
        elif number % 10 == 3:
            ord_suffix = "rd"
        else:
            ord_suffix = "th"
    return f"{name}, you are the {number}{ord_suffix} customer we serve today. Thank you!"