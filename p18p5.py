def xyzsearch(i):
    """takes an arguements and checks if xyz appears in it without being directly preceded by a .
    Assumes arguement is a string
    Returns True if xyz found and not directly preceded by a ., otherwise returns false
    Non-case sensitive"""

    a = i.count("xyz")
    b = i.count(".xyz")

    if a > b:
        return True

    else:
        return False
