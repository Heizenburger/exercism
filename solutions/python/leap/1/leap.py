"""Program to determine whether the given year is a leap year or not"""
def leap_year(year):
    """Function to determine whether input year is a leap year or not
        Input: year(int)
        Output: True/False(boolean)"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False