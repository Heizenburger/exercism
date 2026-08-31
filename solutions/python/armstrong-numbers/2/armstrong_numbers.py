"""Program to determine whether a given number is armstrong number or not"""
def is_armstrong_number(number):
    """ Function to determnie armstrong number
        Input: number (int)
        Output: Boolean"""
    num = number
    armstrong_sum = 0
    expo = len(str(number))
    while num > 0:
        armstrong_sum += (num % 10) ** expo
        num = num // 10
    if number == armstrong_sum:
        return True
    return False        