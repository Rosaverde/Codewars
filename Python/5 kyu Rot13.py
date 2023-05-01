"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""
def rot13(message):
    r = ""
    for i in message:
        c = ord(i)
        if c > 64 and c < 91:
            if c - 78 < 0 :
                c = chr(90 + (c - 77))
            else:
                c = chr(c - 13)
            r = ''.join([r,c])  
        elif c > 96 and c < 123:
            if c - 110 < 0 :
                c = chr(122 + (c - 109))
            else:
                c = chr(c - 13)
            r = ''.join([r,c])
        else:
            r = ''.join([r,chr(c)])
    return r