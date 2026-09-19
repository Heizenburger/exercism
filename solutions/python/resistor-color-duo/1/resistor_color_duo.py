"""This module provides a function which returns a two digit number based on the input colors, even if the input is more than 2 colors"""

color_code = {"black" : 0, "brown" : 1, "red" : 2, "orange" : 3, "yellow" : 4, "green" : 5, "blue" : 6, "violet" : 7, "grey" : 8, "white" : 9}

def value(colors):
    return (int(color_code.get(colors[0])) * 10) + int(color_code.get(colors[1]))
