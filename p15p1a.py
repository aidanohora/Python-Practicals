def funct(n):
    """define a recursive function to take as its single argument an integer
    that is greater than or equal to one and print out that number of terms
    from the series displayed in practical 15
    """
    if  n == 1:
        return 2
    else:
        return n + funct(n - 1)

