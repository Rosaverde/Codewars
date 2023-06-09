"""
Description:

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""
def make_readable(seconds):
    s = int(seconds % 60)
    m = int(((seconds - s)% 3600)/60)
    h = int((seconds - s - m*60)/3600)
    return(f"{h:02d}:{m:02d}:{s:02d}")