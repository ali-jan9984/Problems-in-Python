"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
print(EXPECTED_BAKE_TIME)

def elapsed_baked_time(time_elapsed):
    """Calculate the time the lasagna is in the own
    
    :param time_elapsed: int - baking time already elapsed.
    :return: int - baking time already elapsed from parameter 'time_elapsed'

    Funtion that takes the actual minutes the lasagna has been in the oven as an argument
    and return actual minutes the lasagna has been in the oven based on the param time_elapsed.
    """
    return time_elapsed
elapsed_bake_time = elapsed_baked_time(30)
    

def bake_time_remaining(elapsed_bake):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake

def preparation_time_in_minutes(numbre_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers:int -number of layers
    :return: int - number of minutes it will take based on the number of layers

    Function that takes the number of layers and calculate preparation time in minutes
    based on the number of layers each layer take 2 minutes and after calculating it return
    the number of minutes.
    """
    result = numbre_of_layers * 2
    return result
print(preparation_time_in_minutes(2))
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the number of minutes I have been in the kitchen

    :param number_of_layers:int -number of layers
    :param elapsed_baked_time:int -elapsed back time
    :return: int - number that how many minutes I have been working in the kitchen

    Function that takes the number of layers and elapsed baked time to calculate the total 
    minutes we have been working in the kitche. For calculating the minutes of the number of
    layers we need to call preparation_time_remaining function to get the minutes for the number
    of layers, we will store the result of the function in a variable and after that we will add
    the elapsed_baked_time and the result of the functio and get the total number of minutes
    """
    num_of_min_for_layers = preparation_time_in_minutes(number_of_layers)
    result = num_of_min_for_layers + elapsed_bake_time
    return result
print(elapsed_time_in_minutes(3,20))

    
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.


#  (you can copy and then alter the one from bake_time_remaining.)
