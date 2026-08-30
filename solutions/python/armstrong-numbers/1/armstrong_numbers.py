def is_armstrong_number(number):
    num = number
    sum = 0
    i = len(str(number))
    while num > 0:
        sum += (num % 10) ** i
        num = num // 10
    if number == sum:
        return True
    return False        