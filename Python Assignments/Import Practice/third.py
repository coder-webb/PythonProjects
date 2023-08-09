import second

def one(number):
    return number * 4

def two(number):
    return number - 7

def three(number):
    return one(number) + two(number)

def four(number):
    return second.three(number)