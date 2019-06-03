# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    result = []
    if len(s) % 2 == 1:
        s = s + "_"
    for i in range(0, len(s)-1, 2):
        result.append(s[i]+s[i+1])
    return result


print(solution('abcdef'))

