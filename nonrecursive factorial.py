def fact(number):
    '''Non-recursive function to find the factorial of non-negative integer'''
    if number == 0:
        factorial = 1
    if number == 1:
        factorial = 1
    else:
        product = 1
        for i in range(1, number+1):
            factorial = product*i
            product = factorial
        return factorial


        
