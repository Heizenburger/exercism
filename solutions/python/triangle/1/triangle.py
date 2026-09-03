def equilateral(sides):
    a, b, c = sides
    if not (a > 0 and b > 0 and c > 0):
        return False
    if a + b >= c and b + c >= a and a + c >= b:
        if a == b and b == c and c == a:
            return True
        return False
    return False

def isosceles(sides):
    a, b, c = sides
    if not (a > 0 and b > 0 and c > 0):
        return False
    if a + b >= c and b + c >= a and a + c >= b:
        if a == b or b == c or c == a:
            return True
        return False
    return False
    

def scalene(sides):
    a, b, c = sides
    if not (a > 0 and b > 0 and c > 0):
        return False
    if a + b >= c and b + c >= a and a + c >= b:
        if not (a == b or b == c or c == a):
            return True
        return False
    return False
