"""
Description:

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""
def rgb(r, g, b):
    h = [r,g,b]
    e = {0:"0",1:"1" ,2:"2" ,3:"3" ,4:"4" ,5:"5" ,6:"6" ,7:"7" ,8:"8" ,9:"9" ,10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    q = ""
    for i in h:
        if i > 255:
            q += "".join("FF")
        elif i > 0:
            c = int(i / 16)
            d = (i - (c*16))
            q += str(e[c]) + str(e[d])
        else:
            q += "".join("00")
    return q