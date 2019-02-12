def factorial(x):
    """Function that returns the factorial of its arguement

    Assumes that its arguement is a non-negative integer
    Uses a recursive definition
    """
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
