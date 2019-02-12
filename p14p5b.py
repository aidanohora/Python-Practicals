def fibonacci(x):
    """function to print fibonacci up to a number with arguement x"""
    if x <= 1:
        return x
    else:
        return(fibonacci(x-1) + fibonacci(x-2))

number = 1

while number >= 0:
    number = int(input("Please enter the number to count the fibonacci series up to : "))

    if number < 0:
        print("Negative numbers are not accepted, finishing program...")
    
    else:    
        for i in range(number):
            print(fibonacci(i))




