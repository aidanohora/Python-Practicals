def converttodec(x,y):
    """takes a number x of base y and converts to base 10 notation
    assume x is a string and y is an integer
    return number converted to base selected
    hexadecimals can also be supplied and converted"""


    answer = int(x, base=y)
    return answer

# Reference: https://www.journaldev.com/15068/python-string-to-int-int-to-string#converting-string-to-int-from-different-base
