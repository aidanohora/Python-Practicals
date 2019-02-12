a = str(input("Please enter the word cat: "))
b = str(input("Please enter the word dog: "))

catdog = [a, b]

if catdog.count("cat") == 1 and catdog.count("dog") == 1:
    print("You have entered one cat and one dog, thank you!")

else:
    print("You have not entered one cat and one dog, what a shame.")

