import third

def one(number):
    return number ** 2

def two(number):
    return number * 8

def three(number):
    return one(number) - two(number)


if __name__=='__main__':
    print(three(6))
    print(third.three(6))
    print(third.four(6))