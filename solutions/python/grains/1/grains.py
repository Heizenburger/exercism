"""This module calculates the number of grains of wheat on a chessboard"""

def square(number):
    """This function return the number of grains on a given square"""
    if not 1 <= number <= 64: # when the square value is not in the acceptable range
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
    
def total():
    """This function returns the total number of grains on the chessboard"""
    number = 64
    total_grains = 0
    while number > 0:
        total_grains += square(number)
        number -= 1
    return total_grains