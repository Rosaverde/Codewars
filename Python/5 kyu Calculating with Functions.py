"""
Description:

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))
"""

def zero(*args): 
    if len(args) < 1:
        return '0'
    else:
        return calculation(0, args[0])

def one(*args): 
    if len(args) < 1:
        return '1'
    else:
        return calculation(1, args[0])

def two(*args): 
    if len(args) < 1:
        return '2'
    else:
        return calculation(2, args[0])

def three(*args): 
    if len(args) < 1:
        return '3'
    else:
        return calculation(3, args[0])
def four(*args): 
    if len(args) < 1:
        return '4'
    else:
        return calculation(4, args[0])

def five(*args): 
    if len(args) < 1:
        return '5'
    else:
        return calculation(5, args[0])

def six(*args): 
    if len(args) < 1:
        return '6'
    else:
        return calculation(6, args[0])

def seven(*args): 
    if len(args) < 1:
        return '7'
    else:
        return calculation(7, args[0])

def eight(*args): 
    if len(args) < 1:
        return '8'
    else:
        return calculation(8, args[0])

def nine(*args): 
    if len(args) < 1:
        return '9'
    else:
        return calculation(9, args[0])

def plus(*args):
    for i in args:
        c = '+'+ str(i)
    return c
def minus(*args):
    for i in args:
        c = '-'+ str(i)
    return c

def divided_by(*args):
    for i in args:
        c = '/'+ str(i)
    return c

def times(*args):
    c = '*'+ args[0]
    return c
    
def calculation(a, *args):
    if args[0][0] == '+':
        c = a + int(args[0][1])
    elif args[0][0] == '-':
        c = a - int(args[0][1])
    elif args[0][0] == '*':
        c = a * int(args[0][1])
    elif args[0][0] == '/':
        c = int(a / int(args[0][1]))
    return c