def square_root(x, y):
    """Function to approximate the square root of a number within a tolerance set by the user"""
    
    step = y**2

    root = 0.0

    while abs(x - root**2) >= y and root <= x:
        root += step
    if abs(x - root**2) < y:
            print("The approximate square root of ", x, " is ", root)
    else:
            print("Failed to find a square root of ", x)

y = 0.01

#prompting user for input
x = float(input("Please enter a non-negative integer to approximate the square root of: "))

if x < 0:
    print("Error: Negative numbers not accepted.")

else:
    square_root(x,y)
