"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# This constant should be an integer representing the number of minutes
# the lasagna should bake in the oven. You can use 40 minutes as a default value.
EXPECTED_BAKE_TIME = 40



# Implement the bake_time_remaining() function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
# Implement the preparation_time_in_minutes(number_of_layers) function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :return: int - total preparation time (in minutes).

    Function that returns the total preparation time for the lasagna.
    """
    
    return number_of_layers * 2
    


# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
# Implement the elapsed_time_in_minutes(number_of_layers, elapsed_bake_time) function that has two parameters: number_of_layers (the number of layers added to the lasagna) and elapsed_bake_time (the number of minutes the lasagna has been baking in the oven). This function should return the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    Function that returns the total elapsed time for the lasagna.
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
