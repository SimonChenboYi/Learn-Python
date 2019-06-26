def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False
    if len(array1) == 0:
        return True

    array1.sort()
    array2.sort()

    for i in range(len(array1)):
        if array2[i] != array1[i] * array1[i]:
            return False
    return True

# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python