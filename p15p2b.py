def funct(n):
    """define a recursive function to take as its single argument an integer
    that is greater than or equal to one and print out that number of terms
    from the series displayed in practical 15
    """
    if  n == 1:
        return 1
    else:
        return funct(n - 1) + 2**n-1

number = 1
while number >= 1:
    number = int(input("Please enter an integer greater than or equal to 1: "))
    if number < 1:
        print("The number entered was not greater than or equal to one. Program finishing...")
    else:
        print(funct(number))
