"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one,list_two):
    str_list_one = (str(list_one).strip('[]') + ',')
    str_list_two = (str(list_two).strip('[]') + ',')

    if str_list_one == str_list_two:
        return EQUAL
    if str_list_one in str_list_two:
        return SUBLIST
    if str_list_two in str_list_one:
        return SUPERLIST
    return UNEQUAL