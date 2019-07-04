def sort_array(a):
    odd, even, result = [], [], []
    i, j = 0, 0

    for number in a:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    odd.sort()
    even.sort(reverse= True)

    for number in a:
        if number % 2 == 0:
           result.append(even[i])
           i += 1
        else:
            odd.append(number)
            result.append(odd[j])
            j += 1
    return result


# You are given an array of integers. Your task is to sort odd numbers within the array in ascending order, and even numbers in descending order.
#
# Note that zero is an even number. If you have an empty array, you need to return it.
#
# For example: [5, 3, 2, 8, 1, 4]  -->  [1, 3, 8, 4, 5, 2]
#
# https://www.codewars.com/kata/sort-odd-and-even-numbers-in-different-order/python

