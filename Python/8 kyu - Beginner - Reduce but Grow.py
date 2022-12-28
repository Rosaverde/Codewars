"""
Description:

Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

"""

def grow(arr):
    pass
    sum = 1;    
    for l in arr:
        sum *= l
    return sum