def factorial(x):
    """Function that returns the factorial of its arguement

    Assumes that its arguement is a non-negative integer
    Uses a recursive definition
    """
    if x == 0:
        return 1
    else:
        res = x * factorial(x-1)
        print("Factorial of", x, "is:", res)
        return res

#prompting user for input
number = int(input("Please enter a single non-negative integer to calculate the factorial of: "))

if number < 0:
    print("Error: Non-negative integers are not accepted.")

else:
    print(factorial(number))
