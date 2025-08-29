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

def check_sub_sequence(A,B):
    n1 = len(A)
    n2 = len(B)
    return any(B[i:i+n1] == A for i in range(n2 - n1 + 1))


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if check_sub_sequence(A=list_one,B=list_two):
        return SUBLIST
    if check_sub_sequence(A=list_two,B=list_one):
        return SUPERLIST
    return UNEQUAL