import sys
a=1
cube_root = 0
while a==1:
    cube_root = 0
    number = int(input("Enter the number that you wish to calculate the cube root of: "))

    if number < 0:
        new_number = -number

    elif number == 0:
        print("0 is not accepted by this program. Exiting...")
        sys.exit()

    else:
        new_number = number


    while cube_root**3 < new_number:
        cube_root += 1

    if cube_root**3 == new_number:
            if number < 0:
                cube_root = -cube_root
            print("cube root of", number, "is", cube_root)       

    else:
        print(number, "is not a perfect cube.")

