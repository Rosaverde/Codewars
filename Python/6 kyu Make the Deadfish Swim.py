"""
Description:

Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

    i increments the value (initially 0)
    d decrements the value
    s squares the value
    o outputs the value into the return array

Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
"""
def parse(data):
    c = 0
    e = []
    for i in data:
        if i == 'i':
            c += 1
        elif i == 'd':
            c -= 1
        elif i == 's':
            c = c **2
        elif i == 'o':
            e.append(c)
    return(e)