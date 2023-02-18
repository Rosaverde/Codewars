"""
Description:
Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]

And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
"""
def tower_builder(n_floors):
    f = n_floors * 2 + 1
    h = []
    for i in range(n_floors):
        c = i*2 + 1
        e = int((f - c -1) / 2)
        h.append(f"{e * ' '}{c * '*'}{e * ' '}")
    return h