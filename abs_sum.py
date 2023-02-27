import functools
def abs_sum(list):
    result = functools.reduce(lambda num1, num2: abs(num1) + abs(num2), list, 0)
    return result

list = [-1,2,4,-3]
print(abs_sum(list))