def factorial(n):
    '''Function to calculate and return the factorial of a non-negative integer'''
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return n*factorial(n-1)

print(factorial(6))

    
    
