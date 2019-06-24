from functools import reduce

def persistence(n):
    round = 0
    digtials = list(str(n))

    while len(digtials) > 1:
        digtials = list(str(reduce((lambda x, y: int(x)*int(y)), digtials)))
        round += 1

    return round
