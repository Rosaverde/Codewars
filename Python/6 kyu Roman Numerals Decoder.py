"""
Description:

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI') # should return 21

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""
def solution(roman):
    rc = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    v = 0
    for x in range(len(roman)):
        if x == (len(roman)-1) or rc[roman[x]] >= rc[roman[x+1]]:
            v += rc[roman[x]]
        else:
            v -= rc[roman[x]]
    return v

"""M = 1000 must be added, because the following letter C =100 is lower.
C = 100 must be subtracted because the following letter M =1000 is greater.
M = 1000 must be added, because the following letter L = 50 is lower.
L = 50 must be added, because the following letter I =1 is lower.
I = 1 must be subtracted, because the following letter V = 5 is greater.
V = 5 must be added, because there are no more symbols left."""