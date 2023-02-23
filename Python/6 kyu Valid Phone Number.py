"""
Description:

Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

Examples:

"(123) 456-7890"  => true
"(1111)555 2345"  => false
"(098) 123 4567"  => false
"""
def valid_phone_number(p):
    n = [1,2,3,6,7,8,10,11,12,13]
    if len(p) != 14:
        return False
    for i in n:
        if ord(p[i]) < 47 or ord(p[i]) > 58:
            return False
    if p[0] == '(' and p[4] == ')' and p[5] == ' ' and p[9] == '-':
        return True
    else:
        return False