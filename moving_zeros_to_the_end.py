def move_zeros(array):
    result = []
    count = 0
    for x in array:
        if x is not False and x == 0:
            count += 1
        else:
            result.append(x)
    for i in range(count):
        result.append(0)
    return result


# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python