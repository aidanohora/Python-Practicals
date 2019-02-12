number = int(input("Enter the number for which you wish to calculate the factorial (must be a positive integer): "))

if number < 0:
    print("Please only input positive numbers.")
    number = int(input("Try entering a positive number now: "))
else:
    fact = 1
    i = 1
    while i <= number:
        fact *= i
        i += 1

print("Factorial of", number, "is", fact)


