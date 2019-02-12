def funct(n):
    """define a recursive function to take as its single argument an integer
    that is greater than or equal to one and print out that number of terms
    from the series displayed in practical 15
    """
    if  n == 0:
        return 13
    elif n == 1:
        return 8
    else:
        return funct(n - 2) + 13*funct(n-1)

number = 0
while number >= 0:
    number = int(input("Please enter an integer greater than or equal to 0: "))
    if number < 0:
        print("The number entered was not greater than or equal to 0. Program finishing...")
    else:
        print(funct(number))
