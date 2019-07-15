def repeat_char(string):

    if len(string) == 5:
        return string
    elif len(string) < 5:
        string =  string + string[0]

    return repeat_char(string)

print(repeat_char('j'))



#  Write a function that takes an input character and returns that character repeated 5 times using recursion. For example, if the input is 'g', then the output should be 'ggggg'.
#
# Input: {String} char
# Output: {String}