def fibonacci(x):
    """Function to calculate the first n terms of the fibonacci sequence"""
    if x == 0:
        print("You have requested that no numbers of the fibonacci sequence be displayed. As you wish.")
    else:
        count = 0
        i = 0
        print("0")
        while count < x-1:
            print(i)
            i += 1
            count +=1
        
    return

# prompt user for input
number = int(input("Please enter how many numbers of the fibonacci sequence to display (must be a non-negative integer): "))
if number < 0:
    print("Error: Negative integers are not accepted.")
else:
    fibonacci(number)
