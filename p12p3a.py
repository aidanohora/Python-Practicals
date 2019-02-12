def square_root(x, y):
    """Function to approximate the square root of a number within a tolerance set by the user"""
    
step = y **2

root = 0.0

while abs(x - root**2) >= y and root <= x:
    root += step
    if abs(number - root**2) < y:
        print("The approximate square root of ", x, " is ", root)
    else:
        print("Failed to find a square root of ", number)
