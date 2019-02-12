import sys
a=1
square_root = 0
while a==1:
    number = int(input("Enter the number that you wish to calculate the square root of: "))

    if number < 0:
        print("Negative numbers are not allowed. Exiting the program...")
        sys.exit()

    else:

        while square_root**2 < number:
            square_root += 1

        if square_root**2 == number:
                if number < 0:
                    square_root = -square_root
                print("Square root of", number, "is", square_root)       

        else:
            print(number, "is not a perfect square.")
    



    
