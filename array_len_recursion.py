def getlen(array):

    if array == []:
       length = 0
    else:
        array.pop()
        length = getlen(array) or 0
        length = length + 1

    return length


print(getlen(["Banana", "Orange", "Lemon", "Apple", "Mango"]))



# let a = ["Banana", "Orange", "Lemon", "Apple", "Mango"]
#
# const getLenght = (array) => {
#
# }