def fibonacci(x):
    first = 0
    second = 1
    series = "Fibonacci Series: "
    for i in range(1, x+1):
        if i == 1:
            series += str(first)
        if i == 2:
            series += ", "
            series += str(second)
        else:
            series += ", "
            nth = first + second
            series += str(nth)
            first = second
            second = nth
    return series

number = 1

print("*** Program to print out terms of the Fibonacci series ***")
while number > 0:
    number = int(input("Please enter a positive integer (or non-positive to exit): "))
    if number <= 0:
        print("Non-positive integer received: exiting program...")
    else:
        print(fibonacci(number))
        
