def twostrings(x,y):
    """takes two arguements and checks if either appear at the very end of the other string
    Assumes both arguements are strings
    Returns True if either appears at end of other, otherwise returns false
    Non-case sensitive"""

    x = x.lower()
    y = y.lower()
    
    if len(x) > len(y):
        a = 0 - len(y)
        b = 0
        i = 0
        j = 0
        while i < len(y):
            if x[a] == y[b]:
                j += 1
                a += 1
                b += 1
                i += 1
            else:
                i += len(y)
        if j == len(y):
            return True
        else:
            return False

    elif len(x) == len(y):
        if x == y:
            return True
        else:
            return False

    else:
        a = 0 - len(x)
        b = 0
        i = 0
        j = 0
        while i < len(x):
            if y[a] == x[b]:
                j += 1
                a += 1
                b += 1
                i += 1
            else:
                i += len(x)
        if j == len(x):
            return True
        else:
            return False
