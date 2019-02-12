number = int(input("Enter the number for which you wish to calculate the factorial (must be a positive integer): "))
if number < 0:
    print("Error: Number entered was less than 0. Program will now finish.")
    
while number >= 0:
    if number == 0:
        fact = 1
    elif number == 1:
        fact = 1
    else:
        fact = 1
        i = 1
        while i <= number:
            fact *= i
            i += 1
    print("Factorial of", number, "is", fact)
    number = int(input("Enter the number for which you wish to calculate the factorial (must be a positive integer): ")) 
    if number < 0:
        print("Error: Number entered was less than 0. Program will now finish.")


