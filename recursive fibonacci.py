def printfib(x):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            return fibonacci(n-1) + fibonacci(n-2)
    message = "Fiobonacci: "    
    for n in range(0, x):
        message += str(fibonacci(n))
        if n!=x-1: 
            message += ", "
    print(message)

print("*** Program to print out terms of the Fibonacci series. ***")
while True:
    terms = input("Enter number (non-positive integer to quit): ")
    try:
        terms = int(terms)
    except ValueError:
        print("Please only enter integers.")
    else:
        if terms <= 0:
            print("Quitting program...")
            sys.exit(0)
        else:
            printfib(terms)
        


    
