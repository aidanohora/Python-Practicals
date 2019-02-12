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
        return x[0] == x[-1] and Palin(x[1:-1])

    return Palin(toChars(x))

str = input("Enter a string (empy string to exit): ")

while str != "":
    if Palin(str):
        print(str, "is a paldindrome.")
    else:
        print(str, "is not a paldindrome.")
    str = input("Enter a string (empty string to exit): ")

print("Finished!")

    

    
