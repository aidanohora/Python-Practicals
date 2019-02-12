x = int(input("Please enter an integer: "))

if x == 0:
    print("You have entered a number that is equal to zero.")

elif 0 < x <= 20:
    print("You have entered a number that is between zero and twenty-one.")

elif 20 < x <= 40:
    print("You have entered a number that is between twenty and fourty-one.")

elif 40 < x <= 60:
    print("You have entered a number that is between fourty and sixty-one.")

elif 60 < x <= 80:
    print("You have entered a number that is between sixty and eighty-one.")

elif 80 < x <=100:
    print("You have entered a number that is between eighty and one-hundred-and-one.")

elif x > 100:
    print("You have entered a number greater than one-hundred.")

else:
    print("You have entered a number that is less than zero.")
