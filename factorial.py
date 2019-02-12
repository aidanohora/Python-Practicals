number=int(input("Enter a number: "))
factorial=1
if number==0:
    print("Factorial of 0 is 1")
elif number < 0:
    print("Error: Negative number entered")
else:
    count=0
    while count<number:
        count +=1
        factorial *= count
    print("Factorial of ", number, " is ", factorial)

    
