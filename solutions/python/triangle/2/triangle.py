def equilateral(sides):
    side1, side2, side3 = sides
    if not (side1 > 0 and side2 > 0 and side3 > 0):
        return False
    if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2:
        if side1 == side2 and side2 == side3 and side3 == side1:
            return True
        return False
    return False

def isosceles(sides):
    side1, side2, side3 = sides
    if not (side1 > 0 and side2 > 0 and side3 > 0):
        return False
    if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2:
        if side1 == side2 or side2 == side3 or side3 == side1:
            return True
        return False
    return False
    

def scalene(sides):
    side1, side2, side3 = sides
    if not (side1 > 0 and side2 > 0 and side3 > 0):
        return False
    if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2:
        if not (side1 == side2 or side2 == side3 or side3 == side1):
            return True
        return False
    return False
