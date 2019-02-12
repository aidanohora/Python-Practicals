def Palin(x):
    """checks if string x is a palindrome
    Assumes x is a string
    Returns True if x is a palindrome
    Returns False otherwise
    Non-case sensitive and ignores non-letter characters"""

    def toChars(x):
        """Converts a string to lowercase and removes non-letter
        Assumes x is a str.
        Converts uppercase letters to lowercase and removes symbols"""
        x = x.lower()
        letterstring = ""
        for c in x:
                if c in "abcdefghijklmnopqrstuvwxyz":
                    letterstring += c
        return letterstring
    if len(x) <= 1:
        return True
    else:
        a = 0
        b = -1
        i = 0
        j = 0
        while i < (len(x))//2:
            if x[a] == x[b]:
                j += 1
            a += 1
            b -= 1
            i += 1
        return j == i
            
    return Palin(toChars(x))

    

    
