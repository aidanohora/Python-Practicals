def funct(n):
    """define a recursive function to take as its single argument an integer
    that is greater than or equal to one and print out that number of terms
    from the series displayed in practical 15
    """
    a = n
    n = 0
    while n <= a:
        if  n == 0:
            print("1 gives 13")
            x = 13
            n += 1
        elif n == 1:
            print("1 gives 8")
            y = 8
            n += 1
        else:
            print(n, "gives", x + 13*y)
            z = y
            y = x + 13*y
            x = z
            n += 1

number = 0
while number >= 0:
    number = int(input("Please enter an integer greater than or equal to 0: "))
    if number < 0:
        print("The number entered was not greater than or equal to 0. Program finishing...")
    else:
        funct(number)
