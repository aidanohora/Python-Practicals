x = int(input("Enter a number: "))
while x >= 0:
    if x%2 == 0:
        print(str(x)+" is divisible by 2")
    if x%3 == 0:
        print(str(x)+" is divisible by 3")
    if x%5 == 0:
        print(str(x)+" is divisible by 5")
    if x%7 == 0:
        print(str(x)+" is divisible by 7")
    x = int(input("Enter a number: "))
