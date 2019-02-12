def factorial(x):
    """Function that takes as its single arguement a non-negative
        integer and returns the factorial of the number
        """
    res = 1
    for i in range (1, x+1):
        res *= i
    return res

# prompting user for input

number = int(input("Enter a positive integer: "))

if number >= 0:
    print("The factorial of ", number, " is ", factorial(number))

else:
    print("Error: Only non-negative numbers are accepted. Program finishing...")
    


