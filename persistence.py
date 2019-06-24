from functools import reduce

def persistence(n):
    round = 0
    digtials = list(str(n))

    while len(digtials) > 1:
        digtials = list(str(reduce((lambda x, y: int(x)*int(y)), digtials)))
        round += 1

    return round


# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.