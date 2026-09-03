"""Module to determine if a triangle is equilateral, isosceles, or scalene"""

def equilateral(sides):
    """Function to determine whether the triangle is equilateral or not"""
    side1, side2, side3 = sides
    if not (side1 > 0 and side2 > 0 and side3 > 0):
        return False
    if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2:
        if side1 == side2 and side2 == side3 and side3 == side1:
            return True
        return False
    return False

def isosceles(sides):
    """Function to determine whether the triangle is isosceles or not"""
    side1, side2, side3 = sides
    if not (side1 > 0 and side2 > 0 and side3 > 0):
        return False
    if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2:
        if side1 == side2 or side2 == side3 or side3 == side1:
            return True
        return False
    return False
    

def scalene(sides):
    """Function to determine whether the triangle is scalene or not"""
    side1, side2, side3 = sides
    if not (side1 > 0 and side2 > 0 and side3 > 0):
        return False
    if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2:
        if not (side1 == side2 or side2 == side3 or side3 == side1):
            return True
        return False
    return False
