def funct(n):
    """define a recursive function to take as its single argument an integer
    that is greater than or equal to one and print out that number of terms
    from the series displayed in practical 15
    """
    a = n
    n = 1
    while n <= a:
        if  n == 1:
            print("1 gives 1")
            x = 1
            n += 1
        else:
            print(n, "gives", x + 2**n-1)
            x = x + 2**n-1
            n += 1

number = 1
while number >= 1:
    number = int(input("Please enter an integer greater than or equal to 1: "))
    if number < 1:
        print("The number entered was not greater than or equal to one. Program finishing...")
    else:
        funct(number)
