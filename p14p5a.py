def fibonacci(x):
    """function to print fibonacci up to a number with arguement x"""
    if x <= 1:
        return x
    else:
        return(fibonacci(x-1) + fibonacci(x-2))







